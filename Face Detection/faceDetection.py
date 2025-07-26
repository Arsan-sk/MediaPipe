import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)  
# ↓↓↓ Set the resolution lower to avoid memory overflow with 4K
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cTime = 0   
pTime =0 

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    ret, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # as model train on rgb image
    results = faceDetection.process(imgRGB)
    # print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection) # draw the face detection
            # print(id, detection) # return the id i.e number of faces with other details
            # print(detection.score) #  return score for accuracy for detection of face 
            # print(detection.location_data.relative_bounding_box) # return the bounding box of face

            bboxC = detection.location_data.relative_bounding_box # top left x, top left y, width, height
            h, w, c = img.shape
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                   int(bboxC.width * w), int(bboxC.height * h)
            cv2.rectangle(img, bbox, (255,0,255), 2)
            cv2.putText(img, f'{int(detection.score[0]*100)}%', 
                        (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)
    
    cTime =time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {str(int(fps))}', (20,60), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0) ,3)

    cv2.imshow("Frame", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# RESULTS for the following 
    # print(id, detection)
    #     0 label_id: 0
    # score: 0.921036
    # location_data {
    #   format: RELATIVE_BOUNDING_BOX
    #   relative_bounding_box {
    #     xmin: 0.373758584
    #     ymin: 0.349985
    #     width: 0.362904102
    #     height: 0.483829916
    #   }
    #   relative_keypoints {
    #     x: 0.468315214
    #     y: 0.4783867
    #   }
    #   relative_keypoints {
    #     x: 0.629199743
    #     y: 0.471148908
    #   }
    #   relative_keypoints {
    #     x: 0.550208926
    #     y: 0.586785
    #   }
    #   relative_keypoints {
    #     x: 0.554634631
    #     y: 0.694801748
    #   }
    #   relative_keypoints {
    #     x: 0.387285739
    #     y: 0.533650577
    #   }
    #   relative_keypoints {
    #     x: 0.720285416
    #     y: 0.51692915
    #   }
    # }

    # print(detection.score)
    # [0.9414783716201782]
    # [0.9414783716201782]
    # [0.9372468590736389]
    # [0.9372468590736389]
    
# print(detection.location_data.relative_bounding_box)
    # xmin: 0.411529899
    # ymin: 0.534963608
    # width: 0.345296919
    # height: 0.460376799

    # xmin: 0.411529899
    # ymin: 0.534963608
    # width: 0.345296919
    # height: 0.460376799