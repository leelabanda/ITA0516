import cv2

def overlay_text_on_image(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 0, 255), thickness=2):
    # Convert position tuple to integers
    position = tuple(map(int, position))
    
    # Draw text on the image
    image_with_text = cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    
    return image_with_text

# Example usage:
image_path = 'C:/Users/leela/Pictures/Screenshots/Screenshot (25).png'
text = input("Enter the text to overlay on the image: ")
position = (100, 100)  # Position (x, y) to place the text on the image

# Read the input image
image = cv2.imread(image_path)

# Overlay text on the image
image_with_text = overlay_text_on_image(image, text, position)

# Display the image with the text overlay
cv2.imshow('Image with Text Overlay', image_with_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
