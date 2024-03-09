import cv2
# Read the image
image_path =cv2.imread('C:/Users/leela/Pictures/Screenshots/Screenshot (44).png')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image_path,(11,11),0)

# Display the original and blurred images
cv2.imshow('Original Image', image_path)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
