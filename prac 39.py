import cv2
# Grab the current frame.
my_check , vid = cap.read()
# use counter variable for
# Counting frames
counter = 0
check = True
frame_list = []
while(check == True):
cv2.imwrite("frame%d.jpg" %counter , vid)
check , vid = cap.read()
frame_list.append(vid)
# increment the counter by 1
counter += 1
frame_list.pop()
# looping in the List of frames.
for frame in frame_list:
# show the frame.
cv2.imshow("Frame" , frame)
if cv2.waitKey(25) and 0xFF == ord("q"):
   break
   cap.release()
   # close any open windows
   cv2.destroyAllWindows()
   frame_list.reverse()
   for frame in frame_list:
   cv2.imshow("Frame" , frame)
if cv2.waitKey(25) and 0xFF == ord("q"):
   break
   cap.release()
   cv2.destroyAllWindows()
