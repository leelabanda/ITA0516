import cv2
image=cv2.imread("C:/Users/leela/Pictures/Screenshots/Screenshot (1).png")
cv2.waitKey(0)
cv2.imshow("original",image)
gray_image=cv2.cvtColor(image,
                        cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
