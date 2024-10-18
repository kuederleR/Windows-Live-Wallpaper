import cv2
import numpy as np 
import os
from pynput import keyboard, mouse
import time
import pyautogui

# Get the path to the video file
script_path = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(script_path, "wallpaper.mp4")

def on_activity(*args):
    global last_activity_time
    global video_playing
    # print("Activity detected.")
    last_activity_time = time.time()

    if (video_playing):
        video_playing = False
        # print("Activity detected at: ", last_activity_time)
        # Kill the video if it's playing
        kill_video()

def kill_video():
    global cap
    global video_playing
    # print("Killing Video.")
    try:
        video_playing = False
        # cap.release()
        # cv2.destroyAllWindows()
    except:
        pass
    

def check_activity():
    global video_playing
    global last_activity_time
    global cap
    while True:
        if time.time() - last_activity_time > 5 and not video_playing:
            video_playing = True
            # print("Playing video")
            # Create a named window
            cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
            cv2.setWindowTitle("Video", "Demo Video")
            # Set the window to full screen
            # Change the cursor to grab
            # Move the cursor to the center of the screen
            
            cv2.setWindowProperty("Video", cv2.WND_PROP_TOPMOST, cv2.WINDOW_FULLSCREEN)
            cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            pyautogui.moveTo(0, 0, duration=0.5)
            # Set the title of the window
            # cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

            # cv2.setMouseCallback("Video", lambda *args: None)
            # Hide the cursor in the window
            # cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN | cv2.WINDOW_GUI_NORMAL)
            video_playing = True
            # Open the video file
            cap = cv2.VideoCapture(video_path)
            
            while cap.isOpened() and video_playing:
            # Read a frame from the video
                ret, frame = cap.read()
            
                if not ret:
                    break
            
                # Display the frame in the full screen window
                cv2.imshow("Video", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        time.sleep(1)

video_playing = False
last_activity_time = time.time()
cap = None

# Create keyboard and mouse listeners
keyboard_listener = keyboard.Listener(on_press=on_activity)
mouse_listener = mouse.Listener(on_click=on_activity)
def on_move(x, y):
    on_activity()

mouse_listener = mouse.Listener(on_move=on_move)

mouse_listener.start()  
keyboard_listener.start()

check_activity()

# Release the video capture and close the window
