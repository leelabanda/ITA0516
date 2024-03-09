import cv2
image=cv2.imread("C:/Users/leela/Pictures/Screenshots/Screenshot (44).png")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray_image,100,200)
cv2.imshow("original image",image)
cv2.imshow("canny edge",edges)
cv2.WaitKey(0)
cv2.DestroyAllWindows()
