import numpy as np
import cv2 as cv
import ClickHandler as handler

cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

handler.openGame()
handler.Move()

while True:
    result, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detected = False
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0 ,0), 5)
        roi_gray = gray[x:x+w, y:y+w]
        roi_color = frame[x:x+w, y:y+w]
        face_detected = True
        # eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        
        # for (ex, ey, ew, eh) in eyes:
        #     print("Eye Detected")
        #     cv.rectangle(roi_color, (ex, ey), (ex+ ew, ey + eh), (0, 255, 0), 5)
    
    if face_detected ==  False:
        print("Face Not Detected")
        handler.Hit()
        
            
        
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()