import cv2

def sobel_filter(image_path):
    # Read the input image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Sobel operator in the x-direction
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel operator in the y-direction
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude of the gradient
    gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)

    return gradient_magnitude

# Example usage:
image_path = 'C:/Users/leela/Pictures/Screenshots/Screenshot (44).png'

# Apply Sobel filter to the image
sobel_image = sobel_filter(image_path)

# Display the original and Sobel-filtered images
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Image', original_image)
cv2.imshow('Sobel Filtered Image', sobel_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
