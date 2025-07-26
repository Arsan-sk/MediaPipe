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
        self.results = self.pose.process(rgbFrame)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
        return img


        
    def getPosition(self, img, draw=False):
        ldmList = []
        if self.results.pose_landmarks:
            for id, ldm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(ldm.x*w), int(ldm.y*h)
                ldmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy),5,(255,255,0), cv2.FILLED) 

        return ldmList

    


def main():
    cap = cv2.VideoCapture(0)  
    cTime = 0
    pTime = 0
    detector = poseDetector()

    while True:
        ret, img = cap.read()
        img = detector.findPose(img, draw=True)
        ldmList = detector.getPosition(img)
        if len(ldmList) > 0:
            print(ldmList[0])
            cv2.circle(img, (ldmList[0][1],ldmList[0][2]),5,(255,255,0), cv2.FILLED)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime 

        cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0) ,3)

        cv2.imshow("Frame",img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()





