from os import access
import cv2

frameWidth = 640
frameHeight = 1000

cap = cv2.VideoCapture("Res/scl.mp4")
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

while True:
    sucess,img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("Video",img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
