import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('C:/Users/leela/Pictures/Screenshots/Screenshot (44).png', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and histogram-equalized images side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('Original Image')
axs[1].imshow(equalized_image, cmap='gray')
axs[1].set_title('Histogram Equalized Image')
plt.show()
