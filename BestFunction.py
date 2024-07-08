import cv2

path = "Res/room.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,7),0)

cv2.imshow("room",img)
cv2.imshow("GrayScale",imgGray)
cv2.imshow("Img Blur",imgBlur)
cv2.waitKey(0)