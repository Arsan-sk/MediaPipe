import cv2
import mediapipe as mp
import time

class faceDetector():
    def __init__(self, minDetectionCon = 0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.faceDetection.process(imgRGB)
        bboxes = []
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):

                bboxC = detection.location_data.relative_bounding_box
                h, w, c = img.shape
                bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                    int(bboxC.width * w), int(bboxC.height * h)
                bboxes.append([id, bbox, detection.score])

                if draw:
                    img = self.fancyDraw(img, bbox)
                    cv2.putText(img, f'{int(detection.score[0]*100)}%', 
                                (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)

        return img, bboxes
    
    def fancyDraw(self, img, bbox, l=30, t=5, rt=1):
        x, y, w, h = bbox # top left x, top left y, width, height
        x1, y1 = x+w, y+h # bottom right x, bottom right y
        cv2.rectangle(img, bbox, (255,0,255), rt)
        # Top Left x,y
        cv2.line(img, (x,y),(x+l,y), (255,0,255), t)
        cv2.line(img, (x,y),(x,y+l), (255,0,255), t)
        # Top Right x1,y
        cv2.line(img, (x1,y),(x1-l,y), (255,0,255), t)
        cv2.line(img, (x1,y),(x1,y+l), (255,0,255), t)
        # Bottom Left x,y1
        cv2.line(img, (x,y1),(x+l,y1), (255,0,255), t)
        cv2.line(img, (x,y1),(x,y1-l), (255,0,255), t)
        # Bottom Right x1,y1
        cv2.line(img, (x1,y1),(x1-l,y1), (255,0,255), t)
        cv2.line(img, (x1,y1),(x1,y1-l), (255,0,255), t)

        return img


def main():
    cap = cv2.VideoCapture(0)  
    cTime = 0   
    pTime =0 
    detector = faceDetector()
    while True:
        ret, img = cap.read()
        img, bboxes = detector.findFaces(img)
        print(bboxes)

        cTime =time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {str(int(fps))}', (20,60), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0) ,3)

        cv2.imshow("Frame", img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()