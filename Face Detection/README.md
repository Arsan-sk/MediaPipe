# 📂 Face Detection

## 🧠 Overview
This folder contains scripts that implement face detection using MediaPipe's Face Detection solution. These scripts demonstrate real-time face detection with bounding boxes, confidence scores, and modular implementation patterns for easy integration into larger projects.

## 📘 Learnings & Concepts Covered
- Real-time face detection using MediaPipe
- Bounding box calculation and visualization
- Confidence score display
- Modular design patterns for computer vision tasks
- FPS calculation and performance monitoring
- Custom drawing functions for enhanced visualization

### 🎯 File: `faceDetection.py`
#### 📌 Concept/Goal
- A straightforward implementation of face detection that captures webcam video, processes frames to detect faces, draws bounding boxes around detected faces, and displays confidence scores in real-time.

#### ⚙️ Functions & Methods Used
- `cv2.VideoCapture(0)`: Initializes webcam capture from default camera (index 0). Creates a VideoCapture object to read frames from the camera.
```python
cap = cv2.VideoCapture(0)
```

- `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`: Converts BGR color format to RGB since MediaPipe models are trained on RGB images. This ensures proper color channel ordering for processing.
```python
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `mp.solutions.face_detection.FaceDetection()`: Creates a face detection object with configurable parameters like minimum detection confidence.
```python
faceDetection = mpFaceDetection.FaceDetection()
```

- `cv2.rectangle()`: Draws rectangular bounding boxes around detected faces using calculated pixel coordinates.
```python
cv2.rectangle(img, bbox, (255,0,255), 2)
```

- `cv2.putText()`: Overlays text on the image, used here to display confidence percentages and FPS information.
```python
cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)
```

#### ▶️ How it Works (Step-by-step)
1. Initialize webcam capture and MediaPipe face detection objects
2. Start continuous loop to read frames from webcam
3. Convert each frame from BGR to RGB color space
4. Process the RGB frame through MediaPipe face detection
5. If faces are detected, iterate through each detection
6. Extract relative bounding box coordinates and convert to pixel coordinates
7. Draw purple rectangles around detected faces
8. Display confidence percentage above each bounding box
9. Calculate and display FPS on the frame
10. Show the processed frame in a window
11. Exit loop when 'q' key is pressed

#### 📄 External References
- [MediaPipe Face Detection](https://google.github.io/mediapipe/solutions/face_detection.html)
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)
- [cv2.rectangle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9)

### 🎯 File: `faceDetectionModule.py`
#### 📌 Concept/Goal
- A modular, reusable face detection class that encapsulates face detection functionality with fancy corner-style bounding boxes. This demonstrates object-oriented programming principles for computer vision applications.

#### ⚙️ Functions & Methods Used
- `__init__(self, minDetectionCon = 0.5)`: Constructor that initializes the face detector with configurable minimum detection confidence.
```python
def __init__(self, minDetectionCon = 0.5):
    self.minDetectionCon = minDetectionCon
```

- `findFaces(self, img, draw=True)`: Main method that processes an image and returns detected faces with optional drawing.
```python
def findFaces(self, img, draw=True):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `fancyDraw(self, img, bbox, l=30, t=5, rt=1)`: Custom drawing function that creates stylized corner brackets around faces instead of simple rectangles.
```python
def fancyDraw(self, img, bbox, l=30, t=5, rt=1):
    cv2.line(img, (x,y),(x+l,y), (255,0,255), t)
```

- `cv2.line()`: Used to draw corner brackets by creating lines at each corner of the bounding box, giving a more professional appearance.
```python
cv2.line(img, (x,y),(x+l,y), (255,0,255), t)
```

#### ▶️ How it Works (Step-by-step)
1. Create faceDetector class instance with desired confidence threshold
2. Call findFaces() method with input image and optional draw parameter
3. Convert image to RGB for MediaPipe processing
4. Process image through face detection model
5. For each detected face, extract bounding box coordinates
6. Store detection data (ID, bbox, confidence) in results list
7. If draw=True, call fancyDraw() to create corner-style bounding boxes
8. Draw four corner brackets at each corner of the face bounding box
9. Add confidence percentage text above each detection
10. Return processed image and list of detection data

#### 📄 External References
- [MediaPipe Face Detection](https://google.github.io/mediapipe/solutions/face_detection.html)
- [cv2.line](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2)
- [Object-Oriented Programming in Python](https://docs.python.org/3/tutorial/classes.html)

## ▶️ How to Run
Navigate to the Face Detection folder and run either script:
```bash
cd "Face Detection"
python faceDetection.py
# OR
python faceDetectionModule.py
```

## 📄 Function Documentation
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)
- [cv2.rectangle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9)
- [cv2.putText](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)
- [cv2.line](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html)

## 😎 Fun Fact
MediaPipe's face detection model can detect faces at various angles and lighting conditions with impressive accuracy! It uses a lightweight neural network that's optimized for real-time performance, meaning you can run it on mobile devices and still get smooth 30+ FPS detection rates. The model was trained on diverse datasets to work across different ethnicities, ages, and facial expressions!
