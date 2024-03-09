import cv2
import numpy as np

img = cv2.imread("C:/Users/leela/Pictures/Screenshots/Screenshot (44).png")
cv2.imshow("original image", img)
cv2.waitKey(0)

rows, cols, _ = img.shape  # Get the rows and columns of the input image

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 50], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))
cv2.imshow('Transformed Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
