import cv2
import numpy as np

def opening(image_path, kernel_size):
    # Read the input image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Define the structuring element (kernel) for morphological operations
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)

    # Perform erosion followed by dilation (opening operation)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    return opened_image

# Example usage:
image_path = 'C:/Users/leela/Pictures/Screenshots/Screenshot (31).png'
kernel_size = 5  # Size of the structuring element (kernel)

# Perform opening operation on the image
opened_image = opening(image_path, kernel_size)

# Display the original and opened images
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Image', original_image)
cv2.imshow('Opened Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

