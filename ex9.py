import cv2

# Read the image
image = cv2.imread('C:/Users/leela/Pictures/Screenshots/Screenshot (44).png')

# Resize the image to a larger size
larger_image = cv2.resize(image, (1000, 1000))

# Resize the image to a smaller size
smaller_image = cv2.resize(image, (300, 300))

# Display the original, larger, and smaller images
cv2.imshow('Original Image', image)
cv2.imshow('Larger Image', larger_image)
cv2.imshow('Smaller Image', smaller_image)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
