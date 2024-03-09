import cv2
import numpy as np

# Read the image
image = cv2.imread('C:/Users/leela/Pictures/Screenshots/Screenshot (44).png', cv2.IMREAD_GRAYSCALE)

# Create a kernel for erosion
kernel = np.ones((5,5), np.uint8)

# Erode the image
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
