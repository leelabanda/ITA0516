import cv2
import numpy as np

# Read the image
image_path = 'C:/Users/leela/Pictures/Screenshots/Screenshot (44).png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the original and edged images
cv2.imshow('Original Image', image)
cv2.imshow('Edged Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
