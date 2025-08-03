# 📂 Pose Estimation

## 🧠 Overview
This folder contains scripts that implement real-time pose estimation using MediaPipe's Pose solution. These scripts demonstrate body landmark detection for pose analysis, movement tracking, and fitness applications through advanced 3D modeling of the human body with landmarks for each major joint and part.

## 📘 Learnings & Concepts Covered
- 33-point pose landmark detection and tracking
- Full-body movement tracking and analysis
- Integration of 3D body modeling for pose-based applications
- Real-time joint angle calculation
- Modular design for pose estimation implementations
- Visualizations of pose skeleton and landmark tracking
- Optimization techniques for real-time performance on various devices

### 🎯 File: `poseEstimation.py`
#### 📌 Concept/Goal
- A comprehensive pose estimation implementation that leverages MediaPipe's Pose solution to detect and visualize key body landmarks, offering a complete look at body posture and movement for fitness, dance, and virtual reality applications.

#### ⚙️ Functions & Methods Used
- `cv2.VideoCapture(0)`: Initializes webcam capture from the default camera device to stream live video for pose estimation.
```python
cap = cv2.VideoCapture(0)
```

- `mp.solutions.pose.Pose()`: Creates a pose detection object with configuration options for detecting human poses in a video feed.
```python
pose = mpPose.Pose()
```

- `pose.process(rgbFrame)`: Processes the RGB video frame through MediaPipe's pose detection model to identify body landmarks.
```python
results = pose.process(rgbFrame)
```

- `mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)`: Draws the full-body skeleton connecting all detected landmarks to form a pose structure.
```python
mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
```

- `enumerate(results.pose_landmarks.landmark)`: Iterates through all 33 body landmarks with their IDs for individualized processing and analysis.
```python
for id, ldm in enumerate(results.pose_landmarks.landmark):
```

#### ▶️ How it Works (Step-by-step)
1. Initialize webcam capture and MediaPipe pose detection objects
2. Start continuous video capture loop
3. Read frames from webcam and verify frame integrity
4. Convert BGR frame to RGB for MediaPipe processing
5. Process the RGB frame to detect pose landmarks
6. Verify that pose landmarks are detected properly
7. Visualize the pose skeleton using landmark connections
8. Convert normalized coordinates to pixel coordinates
9. Track and display individual landmark data on the image
10. Calculate FPS for performance evaluation and display
11. Show the processed frame with pose estimation overlay
12. Exit the loop when 'q' key is pressed

#### 📄 External References
- [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose.html)
- [Pose Landmark Model](https://google.github.io/mediapipe/solutions/pose.html#pose-landmark-model)
- [mp.solutions.drawing_utils](https://google.github.io/mediapipe/solutions/drawing_utils.html)
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)

### 🎯 File: `poseModule.py`
#### 📌 Concept/Goal
- A modular, functional pose detector class that encapsulates pose estimation logic, making it simple to integrate pose detection into larger projects with configurable detection parameters for different movement-based applications.

#### ⚙️ Functions & Methods Used
- `__init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5)`: Constructor that initializes the pose detector with customizable parameters for mode, body parts, and confidence thresholds.
```python
def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
    self.mode = mode
    self.upBody = upBody
```

- `findPose(self, img, draw=False)`: Main method that processes an image to detect pose and optionally draws the pose skeleton on the image.
```python
def findPose(self, img, draw=False):
    rgbFrame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `getPosition(self, img, draw=False)`: Extracts position data for all detected pose landmarks and returns them as a list.
```python
def getPosition(self, img, draw=False):
    ldmList = []
```

- `findAngle(self, img, p1, p2, p3, draw=True)`: Calculates the angle formed by three specified landmarks, critical for analyzing joint movement and posture.
```python
def findAngle(self, img, p1, p2, p3, draw=True):
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
```

#### ▶️ How it Works (Step-by-step)
1. Create poseDetector instance with configuration parameters
2. Call findPose() method to process image and detect pose landmarks
3. Convert image from BGR to RGB for MediaPipe detection
4. Process image through MediaPipe pose detection model
5. Visualize the pose structure using landmark connections
6. Call getPosition() to retrieve complete list of pose landmarks
7. Convert normalized coordinates to pixel coordinates for each landmark
8. Optionally display landmark ID numbers or other data on the image
9. Use findAngle() to calculate angles at specified joints for analysis
10. Return processed image and list of landmark data
11. Display calculated angles for pose correction or movement coaching

#### 📄 External References
- [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose.html)
- [Building Modular Code in Python](https://docs.python.org/3/tutorial/modules.html)
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [mp.solutions.drawing_utils](https://google.github.io/mediapipe/solutions/drawing_utils.html)

## ▶️ How to Run
Navigate to the Pose Estimation folder and run either script:
```bash
cd "Pose Estimation"
python poseEstimation.py
# OR
python poseModule.py
```

## 📄 Function Documentation
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)
- [cv2.putText](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [mp.solutions.drawing_utils](https://google.github.io/mediapipe/solutions/drawing_utils.html)

## 😎 Fun Fact
With MediaPipe's Pose solution, you can track all the major joints and parts of the body using 33 landmarks! It's perfect for developing sports analytics apps, fitness trackers, or even interactive dance performances. MediaPipe's high precision ensures that you can accurately measure joint angles, detect movement patterns, or build augmented reality avatars that mimic your movements in real-time! The z-coordinate for each landmark even provides depth information, adding a layer of realism to 3D applications.
