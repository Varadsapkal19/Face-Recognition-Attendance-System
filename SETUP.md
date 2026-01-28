# Setup Instructions

## Quick Setup Guide

### 1. System Requirements

**Minimum:**
- Python 3.7+
- 4GB RAM
- Webcam
- Windows/macOS/Linux

**Recommended:**
- Python 3.8+
- 8GB RAM
- HD Webcam (720p+)

---

### 2. Installation Steps

#### Step 2.1: Install Python

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Step 2.2: Clone Repository

```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
```

#### Step 2.3: Create Virtual Environment (Recommended)

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 2.4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Troubleshooting installation:**

*If `face_recognition` fails to install:*

**Windows:**
```cmd
pip install cmake
pip install dlib
pip install face_recognition
```

**macOS:**
```bash
brew install cmake
pip install dlib
pip install face_recognition
```

**Linux:**
```bash
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev
sudo apt-get install libx11-dev libgtk-3-dev
pip install dlib
pip install face_recognition
```

---

### 3. Dataset Setup

#### Step 3.1: Create Dataset Directory

```bash
mkdir test_dataset
```

#### Step 3.2: Add Person Folders

```bash
mkdir test_dataset/John_Doe
mkdir test_dataset/Jane_Smith
mkdir test_dataset/Alice_Johnson
```

#### Step 3.3: Add Photos

**Photo Guidelines:**
- ✅ File format: .jpg, .jpeg, or .png
- ✅ Front-facing, clear face
- ✅ Good lighting
- ✅ Minimum 500x500 pixels
- ✅ 1-3 photos per person
- ❌ No sunglasses or face coverings
- ❌ No group photos

**Example:**
```
test_dataset/
├── John_Doe/
│   ├── john_front.jpg
│   └── john_side.jpg
└── Jane_Smith/
    └── jane.jpg
```

---

### 4. First Run

#### Step 4.1: Test Installation

```bash
python attendance_system.py
```

**Expected output:**
```
==================================================================
FACE RECOGNITION ATTENDANCE SYSTEM
==================================================================
Loading images from dataset...
Loaded 3 images for classes: {'John_Doe', 'Jane_Smith', 'Alice_Johnson'}
Encoding faces...
Encoding Complete. 3 faces encoded.
Ready to start with 3 known face(s).
```

#### Step 4.2: Test Recognition

1. Position yourself in front of webcam
2. Ensure good lighting
3. Face the camera directly
4. Wait for green box with your name
5. Check `attendance.csv` for your entry

#### Step 4.3: Verify Output

```bash
cat attendance.csv
```

Should show:
```
Name,Date,Time
JOHN_DOE,2026-01-28,14:30:15
```

---

### 5. Configuration (Optional)

#### Adjust Recognition Threshold

Edit `attendance_system.py` line ~140:

```python
if matches[matchIndex] and faceDis[matchIndex] < 0.6:  # Change 0.6
```

**Threshold guide:**
- `0.4` - Very strict
- `0.5` - Strict (high security)
- `0.6` - Balanced (default)
- `0.7` - Loose

#### Change Dataset Path

Edit `attendance_system.py` line ~12:

```python
dataset_path = '/home/claude/test_dataset'  # Change path here
```

---

### 6. Common Issues & Solutions

#### Issue: "No module named 'face_recognition'"
```bash
pip install face_recognition --upgrade
```

#### Issue: "Could not open video stream"
```bash
# Try different camera index
# Edit line: cap = cv2.VideoCapture(1)  # Try 0, 1, 2
```

#### Issue: "No face found in image"
- Use better quality photos
- Ensure face is visible and front-facing
- Check image isn't corrupted

#### Issue: Not recognizing faces
- Add more training photos (2-3 per person)
- Improve lighting conditions
- Lower confidence threshold to 0.7

#### Issue: Too many false positives
- Increase confidence threshold to 0.5
- Use higher quality training photos
- Ensure good lighting during capture

---

### 7. Platform-Specific Notes

#### Windows

**Webcam Permission:**
- Go to Settings → Privacy → Camera
- Enable camera access for Python

**Antivirus:**
- May need to whitelist Python

#### macOS

**Camera Permission:**
```bash
# First run will prompt for camera access
# Or go to System Preferences → Security & Privacy → Camera
```

#### Linux

**Camera Permissions:**
```bash
sudo usermod -a -G video $USER
# Logout and login again
```

**Check camera:**
```bash
ls /dev/video*
# Should show /dev/video0 or similar
```

---

### 8. Next Steps

1. ✅ Add all team members to dataset
2. ✅ Test with each person
3. ✅ Set up regular attendance checking
4. ✅ Export attendance records to Excel
5. ✅ Customize as needed

---

### 9. Getting Help

If you encounter issues:

1. Check [Troubleshooting](README.md#troubleshooting) section
2. Search [GitHub Issues](https://github.com/yourusername/face-recognition-attendance/issues)
3. Create new issue with:
   - Error message
   - Python version (`python --version`)
   - OS details
   - Steps to reproduce

---

**Setup complete! You're ready to go! 🚀**
