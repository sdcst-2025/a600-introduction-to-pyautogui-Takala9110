#!python3
# Demonstration of how to get the current mouse position
import pyautogui
import time

verbose = False
pyautogui.scroll

while True:
    time.sleep(1)
    coordinate = pyautogui.position()
    x,y = pyautogui.position()
    if verbose:
        print(f"The complete coordinate is {coordinate}")
        print(f"You can break them up into x={x} and y={y}")
    else:
        print(coordinate)