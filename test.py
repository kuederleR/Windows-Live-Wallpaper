import cv2
import os

# Path to the video file
script_path = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(script_path, "wallpaper.mp4")

# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Read and display frames from the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was not read successfully, exit the loop
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()