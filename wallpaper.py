import time
from pynput import keyboard, mouse
import subprocess
import os

def on_activity(*args):
    global last_activity_time
    global video_playing
    last_activity_time = time.time()

    if (video_playing):
        video_playing = False
        # print("Activity detected at: ", last_activity_time)
        # Kill the video if it's playing
        kill_vlc()

def kill_vlc():
    try:
        subprocess.run(["taskkill", "/f", "/im", "vlc.exe"], shell=True)
    except:
        pass
def check_activity():
    script_path = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(script_path, "wallpaper.mp4")
    print("VIDEO: ", video_path)
    global last_activity_time
    global video_playing
    while True:
        if time.time() - last_activity_time > 5 and not video_playing:
            # Play video in full screenaa
            # subprocess.run(["explorer", video_path])
            process = subprocess.Popen(["start", "/max", "vlc", "--loop", "--intf", "none", "--no-video-title-show", video_path], shell=True)
            video_playing = True
            # subprocess.run(["vlc", "--fullscreen", video_path])
            last_activity_time = time.time()
        time.sleep(1)

last_activity_time = time.time()
video_playing = False

# Create keyboard and mouse listeners
keyboard_listener = keyboard.Listener(on_press=on_activity)
mouse_listener = mouse.Listener(on_click=on_activity)
def on_move(x, y):
    on_activity()

mouse_listener = mouse.Listener(on_move=on_move)

# Start the listeners
keyboard_listener.start()
mouse_listener.start()

# Start checking for activity
check_activity()

# Join the listeners to keep the main thread alive
keyboard_listener.join()
mouse_listener.join()