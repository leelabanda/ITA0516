import numpy as np
import cv2
def create_white_image_with_rectangle(width, height, rect_start, rect_end):
    white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.rectangle(white_image, rect_start, rect_end, (0, 0, 0), thickness=2)
    return white_image
width = 1000
height = 2000
rect_start = (50, 50)  
rect_end = (200, 150) 
image_with_rectangle = create_white_image_with_rectangle(width, height, rect_start, rect_end)
cv2.imshow('Image with Rectangle', image_with_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
