import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

cTime = 0
pTime = 0
cap = cv2.VideoCapture(0)
hands = htm.HandDetector()

while True:
    ret, img = cap.read() 
    img = hands.findHands(img)
    ldmList = hands.findPosition(img, draw=False) # give list of hand no 0 with its id andxy co.. for all landmark

    if len(ldmList) != 0: # so that notthrough error even if list empty i.e. no hand detected
        print(ldmList[4]) # return id 4ths cx and cy i.e. we successfully track thumb tip
        
        # cv2.circle(img, (ldmList[8][1],ldmList[8][2]), 15, (255,0,255), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime =cTime

    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): 
        break

cap.release()  
cv2.destroyAllWindows()  
