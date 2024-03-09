import cv2
import numpy as np

# load the input image
img = cv2.imread('sudoku.jpg')

# convert the input image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# modify the data type setting to 32-bit floating point
gray = np.float32(gray)

# apply the cv2.cornerHarris method to detect the corners
corners = cv2.cornerHarris(gray, 2, 3, 0.05)

#result is dilated for marking the corners
corners = cv2.dilate(corners, None)

# Threshold for an optimal value.
img[corners > 0.01 * corners.max()]=[0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
