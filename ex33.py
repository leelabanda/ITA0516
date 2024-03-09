import numpy as np
import cv2

def create_white_image_with_rectangle(width, height, rect_start, rect_end):
    # Create a white image of the specified size
    white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    # Draw a rectangle on the white image
    cv2.rectangle(white_image, rect_start, rect_end, (0, 0, 0), thickness=2)
    
    return white_image

# Example usage:
width = int(input("Enter the width of the image: "))
height = int(input("Enter the height of the image: "))
rect_start = (50, 50)  # Starting point of the rectangle (top-left corner)
rect_end = (200, 150)  # Ending point of the rectangle (bottom-right corner)

image_with_rectangle = create_white_image_with_rectangle(width, height, rect_start, rect_end)

# Display the image with the rectangle
cv2.imshow('Image with Rectangle', image_with_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
