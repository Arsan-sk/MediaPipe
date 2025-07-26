import cv2
import time
import poseModule as pm



cap = cv2.VideoCapture(0)  
cTime = 0
pTime = 0
detector = pm.poseDetector()

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
