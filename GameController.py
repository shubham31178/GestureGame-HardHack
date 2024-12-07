import cv2
import mediapipe as mp
import time
import ClickHandler as handler

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 1, 0, 0.5, 0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
handler.openGame()
handler.Move()
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            xTip, yTip, xEnd ,yEnd = 100, 100, 0, 0
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                   xTip, yTip = cx, cy
                   cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 6:
                    xEnd, yEnd = cx, cy
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            xDiff = xTip - xEnd
            yDiff = yTip - yEnd
            if yDiff > 0:
                # print("Finger Down")
                pass
            else:
                # print("Finger Up")
                handler.Hit()
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()