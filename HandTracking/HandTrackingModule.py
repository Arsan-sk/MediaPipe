import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionConf=0.5, trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,max_num_hands=self.maxHands,min_detection_confidence=self.detectionConf,min_tracking_confidence=self.trackConf
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        RGBimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.hands.process(RGBimg) 

        if self.results.multi_hand_landmarks:
            for handsLdm in self.results.multi_hand_landmarks: 
                if draw:
                    self.mpDraw.draw_landmarks(img, handsLdm, self.mpHands.HAND_CONNECTIONS) 

        return img
    

    def findPosition(self, img, handNo=0, draw=True):
        ldmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, ldm in enumerate(myHand.landmark): 
                # print(id,ldm)
                h, w, c = img.shape
                cx , cy = int(w*ldm.x), int(h*ldm.y) 
                ldmList.append([id, cx, cy])
                # print(id,cx,cy)
                if draw:
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

        return ldmList
    
def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    hands = HandDetector()

    while True:
        ret, img = cap.read() 
        img = hands.findHands(img)
        ldmList = hands.findPosition(img, draw=False) # give list of hand no 0 with its id andxy co.. for all landmark

        if len(ldmList) != 0: # so that notthrough error even if list empty i.e. no hand detected
            print(ldmList[4]) # return id 4ths cx and cy i.e. we successfully track thumb tip
            
            cv2.circle(img, (ldmList[8][1],ldmList[8][2]), 15, (255,0,255), cv2.FILLED)


        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime =cTime

        # cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        
        cv2.imshow('frame', img)

        if cv2.waitKey(1) == ord('q'): 
            break

    cap.release()  
    cv2.destroyAllWindows()  



if __name__ == "__main__":
    main()