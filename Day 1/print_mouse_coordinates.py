import pyautogui as pag
import time

def get_mouse_position():
    print("Move your mouse to the attachment button and wait for a few seconds...")
    time.sleep(5)  
    x, y = pag.position()
    print(f"Mouse position: x={x}, y={y}")

get_mouse_position()