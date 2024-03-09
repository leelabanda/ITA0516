import cv2

def capture_and_reverse_video():
    # Open the default camera (usually the webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera")
        return

    # Loop to continuously capture frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is not captured properly, break the loop
        if not ret:
            print("Error: Unable to capture frame")
            break

        # Display the captured frame
        cv2.imshow('Video', frame)

        # Check for key press, if 'q' is pressed, exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

    # Reverse the frames
    frames_reversed = frames[::-1]

    # Display the reversed video
    for frame in frames_reversed:
        cv2.imshow('Reversed Video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

# Call the function to start capturing video and displaying its reverse
capture_and_reverse_video()
