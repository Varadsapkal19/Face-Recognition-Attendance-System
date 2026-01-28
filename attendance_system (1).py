import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pandas as pd

# For testing purposes, we'll create a simple dataset structure
# In production, you would use: path = kagglehub.dataset_download("kdnishanth/characterrecognitionfromnumberplate")

# Create a test dataset directory
dataset_path = '/home/claude/test_dataset'
os.makedirs(dataset_path, exist_ok=True)

# Initialize as empty lists to be populated by the loop
image = []
className = []

# Step 1: Load images and names
print("Loading images from dataset...")
if os.path.exists(dataset_path):
    for person in os.listdir(dataset_path):
        img_path = os.path.join(dataset_path, person)
        if os.path.isdir(img_path):
            for file in os.listdir(img_path):
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_file_path = os.path.join(img_path, file)
                    current_img = cv2.imread(full_file_path)
                    if current_img is None:
                        print(f"Warning: Failed to load image at {full_file_path}. Skipping.")
                    else:
                        image.append(current_img)
                        className.append(person)
    print(f"Loaded {len(image)} images for classes: {set(className)}")
else:
    print(f"Warning: Dataset path '{dataset_path}' does not exist.")
    print("Please create the dataset structure with person folders containing their photos.")

# Step 2: Encode known faces
def findEncodings(images):
    """Extract face encodings from a list of images"""
    encodeList = []
    for idx, img in enumerate(images):
        if img is None:
            print(f"Warning: Skipping a None image at index {idx} during encoding.")
            continue
        
        # Convert BGR to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Find face locations
        face_locations = face_recognition.face_locations(img_rgb)
        
        if face_locations:
            # Get the encoding for the first face found
            encode = face_recognition.face_encodings(img_rgb, face_locations)[0]
            encodeList.append(encode)
        else:
            print(f"Warning: No face found in image at index {idx}. Skipping.")
    
    return encodeList

# Encode all known faces
if image:
    print("Encoding faces...")
    encodeListKnown = findEncodings(image)
    print(f"Encoding Complete. {len(encodeListKnown)} faces encoded.")
else:
    print("No images to encode. Please add images to the dataset.")
    encodeListKnown = []

# Step 3: Function to mark attendance
def markAttendence(name):
    """Mark attendance for a recognized person"""
    csv_file = 'attendance.csv'
    
    # Load or create DataFrame
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['Name', 'Date', 'Time'])
    
    # Get current date and time
    now = datetime.now()
    dtString = now.strftime('%Y-%m-%d')
    timeString = now.strftime('%H:%M:%S')
    
    # Check if attendance for this person on this date is already marked
    if not ((df['Name'] == name) & (df['Date'] == dtString)).any():
        # Add new attendance record
        new_row = pd.DataFrame([{'Name': name, 'Date': dtString, 'Time': timeString}])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(csv_file, index=False)
        print(f"✓ Attendance marked for {name} on {dtString} at {timeString}")
    else:
        print(f"ℹ Attendance already marked for {name} today.")

# Step 4: Start webcam for face recognition
def run_attendance_system():
    """Main function to run the attendance system"""
    if not encodeListKnown:
        print("Error: No encoded faces available. Please add images to the dataset first.")
        return
    
    cap = cv2.VideoCapture(0)  # 0 for default webcam
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        print("Note: Webcam access may not be available in this environment.")
        return
    
    print("Starting attendance system... Press 'q' to quit.")
    
    # Track which faces have been processed to avoid duplicate markings
    processed_faces = set()
    
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab frame")
            break
        
        # Resize for faster processing
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        # Find faces in current frame
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            # Compare with known faces
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            
            if len(faceDis) > 0:
                matchIndex = np.argmin(faceDis)
                
                if matches[matchIndex] and faceDis[matchIndex] < 0.6:  # Confidence threshold
                    name = className[matchIndex].upper()
                    
                    # Scale face location back to original size
                    y1, x2, y2, x1 = [v * 4 for v in faceLoc]
                    
                    # Draw rectangle and label
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    
                    # Mark attendance (once per session per person)
                    if name not in processed_faces:
                        markAttendence(name)
                        processed_faces.add(name)
                else:
                    # Unknown face
                    y1, x2, y2, x1 = [v * 4 for v in faceLoc]
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow('Webcam - Attendance System', img)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Attendance system stopped.")

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("FACE RECOGNITION ATTENDANCE SYSTEM")
    print("=" * 60)
    
    # Check if we can run the system
    if encodeListKnown:
        print(f"\nReady to start with {len(encodeListKnown)} known face(s).")
        print("\nNote: This script requires a webcam to function.")
        print("In a typical environment, uncomment the line below to start:")
        print("# run_attendance_system()")
        print("\nFor testing without webcam, the encoding part has been completed.")
    else:
        print("\nTo use this system:")
        print("1. Create a folder structure: test_dataset/PersonName/photo.jpg")
        print("2. Add photos of people you want to recognize")
        print("3. Run the script again")
