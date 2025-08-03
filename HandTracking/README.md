# 📂 HandTracking

## 🧠 Overview
This folder contains scripts that implement hand tracking and landmark detection using MediaPipe's Hands solution. These scripts demonstrate real-time hand gesture recognition, landmark visualization, and modular hand tracking implementations suitable for gesture-based applications and interactive systems.

## 📘 Learnings & Concepts Covered
- Real-time hand landmark detection and tracking
- 21-point hand landmark visualization
- Hand gesture recognition foundations
- Modular object-oriented design for hand tracking
- Coordinate normalization and pixel conversion
- Multi-hand detection and tracking
- FPS optimization for real-time applications

### 🎯 File: `HandsTracking!st.py`
#### 📌 Concept/Goal
- A comprehensive hand tracking implementation that detects and visualizes all 21 hand landmarks in real-time, with special highlighting of fingertip landmarks for gesture recognition applications.

#### ⚙️ Functions & Methods Used
- `cv2.VideoCapture(0)`: Initializes webcam capture from the default camera device to stream live video frames.
```python
cap = cv2.VideoCapture(0)
```

- `mp.solutions.hands.Hands()`: Creates a hands detection object with configurable parameters for detection and tracking confidence.
```python
hands = mpHands.Hands()
```

- `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`: Converts BGR color format to RGB as MediaPipe models are trained on RGB images for optimal performance.
```python
RGBimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `hands.process(RGBimg)`: Processes the RGB image through MediaPipe to detect hand landmarks and returns detection results.
```python
results = hands.process(RGBimg)
```

- `enumerate(handsLdm.landmark)`: Iterates through all 21 hand landmarks with their IDs (0-20) for individual landmark processing.
```python
for id, ldm in enumerate(handsLdm.landmark):
```

- `cv2.circle()`: Draws filled circles at specific landmark positions, particularly highlighting fingertip landmarks (0,4,8,12,16,20).
```python
cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
```

- `mp.solutions.drawing_utils.draw_landmarks()`: Draws connections between hand landmarks to visualize the complete hand structure.
```python
mpDraw.draw_landmarks(img, handsLdm, mpHands.HAND_CONNECTIONS)
```

#### ▶️ How it Works (Step-by-step)
1. Initialize webcam capture and MediaPipe hands detection objects
2. Start continuous video capture loop
3. Read frames from webcam and convert BGR to RGB
4. Process RGB frame through MediaPipe hands detection
5. Check if hand landmarks are detected in the frame
6. For each detected hand, iterate through all 21 landmarks
7. Convert normalized coordinates (0-1) to pixel coordinates
8. Highlight specific landmarks (fingertips) with filled circles
9. Draw skeletal connections between landmarks using HAND_CONNECTIONS
10. Calculate and display real-time FPS on the frame
11. Display processed frame with hand tracking overlay
12. Exit when 'q' key is pressed

#### 📄 External References
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [Hand Landmark Model](https://google.github.io/mediapipe/solutions/hands.html#hand-landmark-model)
- [cv2.circle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)

### 🎯 File: `HandTrackingModule.py`
#### 📌 Concept/Goal
- A modular, reusable HandDetector class that encapsulates hand tracking functionality, making it easy to integrate hand detection into other projects with clean, object-oriented code structure.

#### ⚙️ Functions & Methods Used
- `__init__(self, mode=False, maxHands=2, detectionConf=0.5, trackConf=0.5)`: Constructor that initializes the hand detector with customizable parameters for detection mode, maximum hands, and confidence thresholds.
```python
def __init__(self, mode=False, maxHands=2, detectionConf=0.5, trackConf=0.5):
    self.mode = mode
    self.maxHands = maxHands
```

- `findHands(self, img, draw=True)`: Main method that processes an image to detect hands and optionally draws landmark connections.
```python
def findHands(self, img, draw=True):
    RGBimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- `findPosition(self, img, handNo=0, draw=True)`: Extracts landmark positions for a specific hand and returns them as a list of [id, x, y] coordinates.
```python
def findPosition(self, img, handNo=0, draw=True):
    ldmList = []
```

- `self.mpHands.Hands()`: Creates MediaPipe hands object with custom parameters passed from the constructor.
```python
self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands)
```

#### ▶️ How it Works (Step-by-step)
1. Create HandDetector instance with desired configuration parameters
2. Call findHands() method to process image and detect hand landmarks
3. Convert image from BGR to RGB for MediaPipe processing
4. Process image through MediaPipe hands detection model
5. If hands detected and draw=True, visualize landmark connections
6. Call findPosition() to extract specific hand landmark coordinates
7. Select specific hand (handNo parameter) from detected hands
8. Convert normalized coordinates to pixel positions for each landmark
9. Store landmark data as [id, x, y] in a list for easy access
10. Optionally draw circles at landmark positions for visualization
11. Return processed image and landmark position list

#### 📄 External References
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [Python Classes and Objects](https://docs.python.org/3/tutorial/classes.html)
- [cv2.circle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670)

### 🎯 File: `ModuleTest.py`
#### 📌 Concept/Goal
- A demonstration script that shows how to use the HandTrackingModule class, specifically highlighting how to track individual landmarks like the index finger tip for gesture recognition applications.

## ▶️ How to Run
Navigate to the HandTracking folder and run any of the scripts:
```bash
cd HandTracking
python "HandsTracking!st.py"
# OR
python HandTrackingModule.py
# OR
python ModuleTest.py
```

## 📄 Function Documentation
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html)
- [cv2.circle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670)
- [cv2.putText](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html)
- [mp.solutions.drawing_utils](https://google.github.io/mediapipe/solutions/drawing_utils.html)

## 😎 Fun Fact
MediaPipe's hand tracking model can detect 21 different landmarks on each hand with incredible precision! It can track up to 2 hands simultaneously at 30+ FPS. The coolest part? Each landmark has a 3D coordinate (x, y, z), so you can build applications that understand hand depth and create amazing augmented reality experiences. The model was trained on hundreds of thousands of hand images from different angles, lighting conditions, and skin tones to work universally!
