import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose() # its params as follow with there default value
# static_image_mode = false same detect when confidence high when true
# upper_body_only = False toat 35 body landmarks its detect wher 25 are upeper body part and thats what thois define to detect all or just upper_body_only
# smooth_landmark = True 
# min_detection_confidence = 0.5 fordetection of pose do only when have a confidence as set
# min_tracking_confidence = 0.5 if detected thenstart tracking do only when have a confidence as set



cap = cv2.VideoCapture(0)  


cTime = 0
pTime = 0

while True:
    ret, frame = cap.read()
    
    # Check if frame was successfully read
    if not ret:
        print("Failed to grab frame. Exiting...")
        break
        
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # as model trained on rgb frames / images

    results = pose.process(rgbFrame)
    # print(results.pose_landmarks)
    # landmark {
    # x: 0.601654887
    # y: 3.5217073
    # z: -0.0315892845
    # visibility: 0.000107777574

    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, ldm in enumerate(results.pose_landmarks.landmark):
            # print(id,ldm) 
            h, w, c = frame.shape
            cx, cy = int(ldm.x*w), int(ldm.y*h)
            cv2.circle(frame, (cx,cy),5,(255,255,0), cv2.FILLED) 

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime 

    cv2.putText(frame, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0) ,3)

    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()