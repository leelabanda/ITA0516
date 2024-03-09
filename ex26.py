import cv2

def reverse_video(input_video_path, output_video_path):
    # Open the input video file
    input_video = cv2.VideoCapture(input_video_path)
    
    # Get the properties of the input video
    fps = input_video.get(cv2.CAP_PROP_FPS)
    frame_count = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Create a VideoWriter object to write the output video
    output_video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
    
    # Read and write each frame in reverse order
    for frame_number in range(frame_count - 1, -1, -1):
        # Set the frame position
        input_video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        
        # Read the frame
        ret, frame = input_video.read()
        
        if not ret:
            break
        
        # Write the frame to the output video
        output_video.write(frame)
        
        # Display progress
        print(f"Writing frame {frame_number}/{frame_count}")
    
    # Release the video objects
    input_video.release()
    output_video.release()
    
    print("Video reversed successfully!")

# Example usage:
input_video_path = '‪C:/Users/leela/Pictures/Screenshots'
output_video_path = 'D:/New folder'
reverse_video(input_video_path, output_video_path)
