import numpy as np
import cv2

def create_colored_boxes_image(image_size):
    # Create a white image of the specified size
    white_image = np.ones((image_size[1], image_size[0], 3), dtype=np.uint8) * 255

    # Calculate the size of the colored boxes (1/10th of the image size)
    box_size = (image_size[0] // 10, image_size[1] // 10)

    # Create black, blue, green, and red boxes in each corner
    white_image[:box_size[1], :box_size[0]] = [0, 0, 0]  # Black box in the top-left corner
    white_image[:box_size[1], -box_size[0]:] = [255, 0, 0]  # Blue box in the top-right corner
    white_image[-box_size[1]:, :box_size[0]] = [0, 255, 0]  # Green box in the bottom-left corner
    white_image[-box_size[1]:, -box_size[0]:] = [0, 0, 255]  # Red box in the bottom-right corner

    return white_image

# Example usage:
image_size = (400, 300)  # Specify the size of the image (width, height)
colored_boxes_image = create_colored_boxes_image(image_size)

# Display the image
cv2.imshow('Colored Boxes Image', colored_boxes_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
