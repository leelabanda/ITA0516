import cv2

def detect_smiles(image_path):
    # Load the pre-trained Haar Cascade Classifier for smile detection
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect smiles in the image
    smiles = smile_cascade.detectMultiScale(gray_image, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
    
    # Draw rectangles around the detected smiles
    for (x, y, w, h) in smiles:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the image with the detected smiles
    cv2.imshow('Detected Smiles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
image_path = 'C:/Users/leela/Desktop/html/picture.png'
detect_smiles(image_path)
