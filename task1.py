import pyautogui as p
import tkinter as tk
from PIL import Image, ImageTk
import time
import sys
import keyboard

p.FAILSAFE = False

running = True


path = [
    (408, 634),
    (519, 636),
    (510, 575),
    (692, 573),
    (692, 644),
    (763, 644),
    (759, 471),
    (872, 478),
    (871, 422),
    (923, 422),
    (926, 468),
    (997, 461),
    (997, 425),
    (1067, 424),
]

def stop_program(event=None):
    global running
    running = False
    print("ESC pressed. Exiting...")
    root.destroy()
    sys.exit()

def run_maze():

    p.moveTo(path[0][0], path[0][1], duration=0.5)


    for x, y in path[1:]:
        p.moveTo(x, y, duration=0.5)
        time.sleep(0.5)

    print("Maze complete!")

root = tk.Tk()
root.state("zoomed")
root.title("Maze")

image = Image.open("Maze.png")
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()


root.after(3000, run_maze)

root.mainloop()