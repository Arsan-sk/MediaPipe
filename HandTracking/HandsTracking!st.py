import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands # creat hands object --It necessary to write a [solutions] before any method of mediapipe
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
 # method for drawing points at landmarks as well as line between them as manually its required tomuch mathematics using prebuilt one

cTime = 0
pTime = 0

while True:

    ret, img = cap.read() #its take 5 parameters which are default as follow with there default values
    # static_image__mode = false --its stop hand tracking if confidence is less than set, for detection instead of continuous tracking while oppsite for true
    # max_num_hands = 2 --its set the number of maximum hands
    # min_detection_confidence = 0.5 --i.e 50% confidence for detecting hands is set
    # min_tracking_confidence = 0.5 --same as previous one

    RGBimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # change torgb for processing as mediapipe trained andwork on rgb image
    results = hands.process(RGBimg) # this will process and locate landmarks in rgb image and return them
    # print(results.multi_hand_landmarks) # multi_hand_landmarks return coordinates for hand landmarks
        # landmark {
        # x: 0.280216753
        # y: 0.456834435
        # z: -0.100757822
        # }
        # landmark {
        # x: 0.276438415
        # y: 0.377739191
        # z: -0.111736827  -- An array of landmarks

    if results.multi_hand_landmarks: # bcz of this we dont face error even if no hands detected
        for handsLdm in results.multi_hand_landmarks: # for each landmarks in array
            for id, ldm in enumerate(handsLdm.landmark): # give all landmarks with id 
                # print(id,ldm)
                # 0 x: 0.586640477
                # y: 0.941954136
                # z: 7.62740683e-007

                # 1 x: 0.667436779
                # y: 0.873289704
                # z: -0.0277191736

                h, w, c = img.shape
                cx , cy = int(w*ldm.x), int(h*ldm.y) # We get landmark coordinates as normalized decimals (0–1), so we multiply by image width/height to convert them to actual pixel positions on the image.
                # print(id, cx, cy) # print accurate location co-ordinate of each landmark on framewith its id
                # 0 348 478
                # 1 438 447
                # 2 511 391
                # 3 551 333

                if id in [0,4,8,12,16,20]:
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
                # cv2.circle(img, (cx,cy), 7, (255,0,255), 10, -1)
            mpDraw.draw_landmarks(img, handsLdm, mpHands.HAND_CONNECTIONS) # HAND_CONNECTION drwal line between points while without it its just a points at landmarks

# fps calculation as if 1frame in 1sec it 1/1 hence 1 1 frame in 0.02 second is1/0.02 i.e 50fps
    # Calculate Frames Per Second (FPS)
    # cTime is the current time, pTime is the time at the previous frame
    # The difference (cTime - pTime) gives the time taken to process one frame
    # FPS is the inverse of that time (1 second divided by time per frame)
    # Then we update pTime to the current time for the next loop
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime =cTime

    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): # wait for a key press, if 'q' is pressed, exit the loop where ord('q') is used to get the ASCII value of 'q'
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Destroy all the windows created by OpenCV