# import the necessary packages 
import cv2 

# read the image 
img = cv2.imread("your image path", 0) 

# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 

# define the kernel 
kernel = np.ones((13, 13), np.uint8) 

# use morph gradient 
morph_gradient = cv2.morphologyEx(binr, 
								cv2.MORPH_TOPHAT, 
								kernel) 
# print the output 
plt.imshow(morph_gradient, cmap='gray') 
