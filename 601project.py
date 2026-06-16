import pyautogui as p
import keyboard
import time

time.sleep(3)

cookx, cooky = 216, 430

upgrade = [
    (1157, 127),
    ( 1194, 126),
]

build = [
    (1200, 231),
    (1224, 288),
    (1202, 282),
    (1205, 352),
    (1232, 411),
    (1215, 476),
    (1216, 568),
    (1211, 610),
    (1211, 660),
    (1211, 710),
]

build2 = [
    (1200, 231),
    (1224, 288),
    (1202, 282),
    (1205, 352),
    (1232, 411),
    (1215, 476),
    (1216, 568),
    (1211, 610),
    (1211, 660),
    (1211, 710),
    (1211, 760),
    (1211, 815),
]



running = True

def stop_script():
    global running
    running = False
    print("ESC pressed. Exiting...")

keyboard.add_hotkey("esc", stop_script)

while running:
    for _ in range(40):
        if not running:
            break

        p.click(cookx, cooky)
        time.sleep(0.005)

    if not running:
        break

    p.move(1292, 418)

    p.scroll(50000000)
    time.sleep(0.2)

    p.scroll(-100)
    time.sleep(0.2)

    for x, y in upgrade:
        if not running:
            break

        p.click(x, y)
        time.sleep(0.1)

    p.move(736, 404)
    time.sleep(0.5)

    for x, y in build:
        if not running:
            break

        p.click(x, y)
        time.sleep(0.1)

    p.scroll(-500)

    for x, y in build2:
        if not running:
            break

        p.click(x, y)
        time.sleep(0.1)

    p.scroll(-500)

    for x, y in build2:
        if not running:
            break

        p.click(x, y)
        time.sleep(0.1)

print("Script stopped.")

