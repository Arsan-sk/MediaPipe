import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, enable_segmentation=self.upBody, smooth_landmarks=self.smooth, min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)

    def findPose(self,img, draw=False):
        rgbFrame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # as model trained on rgb frames / images
        results = self.pose.process(rgbFrame)

        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
        return img


        
    
        for id, ldm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(ldm.x*w), int(ldm.y*h)
            cv2.circle(frame, (cx,cy),5,(255,255,0), cv2.FILLED) 

    


def main():
    cap = cv2.VideoCapture(0)  
    cTime = 0
    pTime = 0
    detector = poseDetector()

    while True:
        ret, frame = cap.read()
        frame = detector.findPose(frame, draw=True)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime 

        cv2.putText(frame, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0) ,3)

        cv2.imshow("Frame",frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()





