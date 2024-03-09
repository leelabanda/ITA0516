import cv2
import numpy as np

# Read the image
image = cv2.imread('C:/Users/leela/Pictures/Screenshots/Screenshot (44).png')

# Determine the dimensions of the image
height, width = image.shape[:2]

# Define the center of rotation
center = (width // 2, height // 2)

# Define the rotation matrix for 90 degrees clockwise rotation along the y-axis
rotation_matrix = cv2.getRotationMatrix2D(center, 90 , 1)

# Perform perspective transformation to simulate 90-degree clockwise rotation along the y-axis
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
