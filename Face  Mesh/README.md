# 📂 Face Mesh

## 🧠 Overview
This folder contains scripts that implement face mesh detection using MediaPipe's Face Mesh solution. These scripts demonstrate detailed facial landmark detection with 468 precise points, creating a complete 3D mesh overlay on faces for advanced facial analysis, AR applications, and detailed facial feature tracking.

## 📘 Learnings & Concepts Covered
- High-precision face mesh detection with 468 landmarks
- 3D facial geometry reconstruction
- Face tesselation and mesh visualization
- Multi-face detection and tracking
- Advanced facial landmark analysis
- Modular face mesh implementation patterns
- Real-time facial feature mapping

### 🎯 File: `faceMesh.py`
#### 📌 Concept/Goal
- A comprehensive face mesh implementation that detects and visualizes detailed facial landmarks using MediaPipe's Face Mesh solution, creating a complete mesh overlay on detected faces for advanced facial analysis applications.

#### ⚙️ Functions & Methods Used
- `cv2.VideoCapture(0)`: Initializes webcam capture from the default camera device for real-time face mesh detection.
```python
cap = cv2.VideoCapture(0)
```

- `mp.solutions.face_mesh.FaceMesh(max_num_faces=2)`: Creates a face mesh detection object configured to detect up to 2 faces simultaneously in the frame.
```python
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
```

- `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`: Converts BGR color format to RGB as MediaPipe face mesh models are optimized for RGB input images.
```python
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `faceMesh.process(imgRGB)`: Processes the RGB image through MediaPipe's face mesh detection algorithm to identify facial landmarks.
```python
results = faceMesh.process(imgRGB)
```

- `mp.solutions.drawing_utils.DrawingSpec()`: Creates drawing specifications for customizing the appearance of face mesh visualization including thickness, radius, and color.
```python
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))
```

- `mpDraw.draw_landmarks()`: Draws the complete face mesh tesselation connecting all 468 facial landmarks with lines and points.
```python
mpDraw.draw_landmarks(img, faceLdms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)
```

- `enumerate(faceLdms.landmark)`: Iterates through all 468 facial landmarks with their respective IDs for individual landmark processing.
```python
for id,lm in enumerate(faceLdms.landmark):
```

#### ▶️ How it Works (Step-by-step)
1. Initialize webcam capture and MediaPipe face mesh detection objects
2. Configure drawing specifications for mesh visualization
3. Start continuous video capture loop
4. Read frames from webcam and convert BGR to RGB
5. Process RGB frame through MediaPipe face mesh detection
6. Check if face landmarks are detected in the frame
7. For each detected face, access all 468 facial landmarks
8. Draw complete face mesh tesselation with custom styling
9. Convert normalized coordinates to pixel coordinates for each landmark
10. Calculate and display real-time FPS on the frame
11. Display processed frame with face mesh overlay
12. Exit when 'q' key is pressed

#### 📄 External References
- [MediaPipe Face Mesh](https://google.github.io/mediapipe/solutions/face_mesh.html)
- [Face Mesh Model](https://google.github.io/mediapipe/solutions/face_mesh.html#face-landmark-model)
- [mp.solutions.drawing_utils](https://google.github.io/mediapipe/solutions/drawing_utils.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)

### 🎯 File: `faceMeshModule.py`
#### 📌 Concept/Goal
- A modular, object-oriented face mesh detector class that encapsulates face mesh functionality for easy integration into larger projects, with additional features like landmark ID visualization and customizable mesh drawing.

#### ⚙️ Functions & Methods Used
- `__init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackingCon=0.5)`: Constructor that initializes the face mesh detector with configurable parameters for static mode, maximum faces, and confidence thresholds.
```python
def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackingCon=0.5):
    self.staticMode = staticMode
    self.maxFaces = maxFaces
```

- `findFaceMesh(self, img, draw=True)`: Main method that processes an image to detect face meshes and optionally draws the mesh tesselation.
```python
def findFaceMesh(self, img, draw=True):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `self.mpFaceMesh.FaceMesh()`: Creates MediaPipe face mesh object with custom parameters passed from the constructor.
```python
self.faceMesh = self.mpFaceMesh.FaceMesh(static_image_mode=self.staticMode, max_num_faces=self.maxFaces)
```

- `cv2.putText()`: Adds landmark ID numbers directly on the image at each landmark position for detailed facial point identification.
```python
cv2.putText(img, str(id), (cx,cy), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,0), 1)
```

- `self.mpDraw.draw_landmarks()`: Draws the face mesh tesselation with custom drawing specifications for professional visualization.
```python
self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION, self.drawSpec, self.drawSpec)
```

#### ▶️ How it Works (Step-by-step)
1. Create faceMeshDetector instance with desired configuration parameters
2. Call findFaceMesh() method to process image and detect facial landmarks
3. Convert image from BGR to RGB for MediaPipe processing
4. Process image through MediaPipe face mesh detection model
5. If faces detected and draw=True, visualize complete mesh tesselation
6. For each detected face, iterate through all 468 landmarks
7. Convert normalized coordinates to pixel positions for each landmark
8. Optionally display landmark ID numbers on the image
9. Store landmark data as [x, y] coordinates for each face
10. Return processed image and list of face landmark arrays
11. Display face count information for debugging purposes

#### 📄 External References
- [MediaPipe Face Mesh](https://google.github.io/mediapipe/solutions/face_mesh.html)
- [Face Mesh Connections](https://google.github.io/mediapipe/solutions/face_mesh.html#face-landmark-model)
- [Python Classes and Objects](https://docs.python.org/3/tutorial/classes.html)
- [cv2.putText](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)

## ▶️ How to Run
Navigate to the Face Mesh folder and run either script:
```bash
cd "Face  Mesh"
python faceMesh.py
# OR
python faceMeshModule.py
```

## 📄 Function Documentation
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)
- [cv2.putText](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [mp.solutions.drawing_utils](https://google.github.io/mediapipe/solutions/drawing_utils.html)
- [mp.solutions.face_mesh](https://google.github.io/mediapipe/solutions/face_mesh.html)

## 😎 Fun Fact
MediaPipe's Face Mesh can detect an incredible 468 3D facial landmarks in real-time! That's enough precision to track subtle facial expressions, eye movements, and even lip-sync for digital avatars. The model creates a complete 3D mesh of your face that could be used for virtual makeup try-ons, facial expression analysis for emotion recognition, or even creating personalized emojis. Each landmark has x, y, and z coordinates, making it perfect for AR applications that need to understand face depth and orientation!
