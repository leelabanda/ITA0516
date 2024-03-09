import cv2
import numpy as np
image_path=cv2.imread("C:/Users/leela/Pictures/Screenshots/Screenshot (44).png")
kernal=np.ones((5,5),np.uint8)
erode_image=cv2.erode(image_path,kernal,iterations=1)
cv2.imshow("image",image_path)
cv2.imshow("erosion imahe",erode_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
