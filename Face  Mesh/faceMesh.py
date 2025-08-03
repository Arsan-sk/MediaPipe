import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
cTime = 0
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0)) # for hd 4k video increase thickness and radius to 2 or more

while True:
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks: # if detected
        for faceLdms in results.multi_face_landmarks: # give multiple faces
            mpDraw.draw_landmarks(img, faceLdms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)

            for id,lm in enumerate(faceLdms.landmark): # give land marks for each face
                # print(lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id,cx,cy)
                



    cTime = time.time()
    fps = 1 / (cTime - pTime)   
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




# lm:
# x: 0.679614842
# y: 0.543312132
# z: 0.0177986715

# x: 0.685733259
# y: 0.535742879
# z: 0.0185800884

# cx, cy 
# 408 329
# 429 276
# 424 277
# 421 278

# id,cx,cy
# 0 400 369
# 1 403 329
# 2 400 342
# 3 392 293
# .
# .
# .
# .
# 466 469 273
# 467 474 268