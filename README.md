# 📂 MediaPipe

## 🧠 Overview
This repository serves as a collection of advanced scripts that utilize the MediaPipe library for various computer vision tasks including face mesh, hand tracking, face detection, and pose estimation. Suitable for learners interested in enhancing their computer vision skills using Python and OpenCV.

## 📘 Learnings & Concepts Covered
- Real-time face detection and mesh analysis.
- Hand landmark tracking and gesture detection.
- Pose estimation using body landmarks.
- Integration of MediaPipe solutions for efficient video processing.

### 🎯 File: `Face Mesh`
#### 📌 Concept/Goal
- Implements face mesh detection using MediaPipe's Face Mesh solution, allowing for intricate detection and visualization of facial landmarks.

#### ⚙️ Functions & Methods Used
```python
cv2.VideoCapture()
cv2.cvtColor()
cv2.imshow()
```
- `cv2.VideoCapture()`: Initializes video capture. Handles frame collection from webcam.
- `cv2.cvtColor()`: Converts color spaces to align with model inputs.
- `cv2.imshow()`: Displays video frames, providing real-time visualization.

#### ▶️ How it Works (Step-by-step)
1. Capture frames from the webcam.
2. Convert frames to RGB for MediaPipe processing.
3. Detect face landmarks if a face is present.
4. Draw detected landmarks on the frame.
5. Display the frame with landmarks.

#### 📄 External References
- [OpenCV Documentation](https://docs.opencv.org)
- [MediaPipe Documentation](https://mediapipe.dev)

### 🎯 File: `Hand Tracking`
#### 📌 Concept/Goal
- Utilizes the MediaPipe Hands solution to track and visualize hand landmarks for gesture detection.

#### ⚙️ Functions & Methods Used
```python
cv2.VideoCapture()
cv2.resize()
cv2.cvtColor()
cv2.imshow()
```
- `cv2.VideoCapture()`: Captures live video for processing.
- `cv2.cvtColor()`: Converts frames to appropriate color space for landmark detection.
- `cv2.imshow()`: Showcases real-time processed frames.

#### ▶️ How it Works (Step-by-step)
1. Access webcam feed.
2. Convert frames to RGB.
3. Analyze frames using MediaPipe to detect hands.
4. Annotate frames with hand landmarks.
5. Present the annotated frame.

#### 📄 External References
- [OpenCV Documentation](https://docs.opencv.org)
- [MediaPipe Documentation](https://mediapipe.dev)

... (Repeat for each section of the project including additional files such as Pose Estimation, Face Detection)

## ▶️ How to Run
Open a terminal in each directory and run:
```shell
python <script_name>.py
```

## 📄 Function Documentation
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html)

## 😎 Fun Fact
Did you know? MediaPipe can process video at lightning speeds, often reaching up to 30 frames per second even on average hardware. This makes it excellent for interactive applications like virtual try-ons or gaming!