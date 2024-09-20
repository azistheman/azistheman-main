from pynput.mouse import Button, Controller, Listener
import time
import threading

mouse = Controller()
click_interval = 0.01
auto_clicking = False
click_mode = 'left'

def clicker():
    while True:
        if auto_clicking:
            if click_mode == 'left':
                mouse.click(Button.left, 1)
                mouse.release(Button.left)
            elif click_mode == 'right':
                mouse.click(Button.right, 1)
                mouse.release(Button.right)
            elif click_mode == 'both':
                mouse.click(Button.left, 1)
                mouse.click(Button.right, 1)
            time.sleep(click_interval)

def on_click(x, y, button, pressed):
    global auto_clicking
    if button == Button.left:
        if pressed:
            auto_clicking = True
        else:
            auto_clicking = False

def get_click_mode():
    global click_mode
    print("Choose your click mode (default is left):\n")
    print("1: Left")
    print("2: Right")
    print("3: Left & Right\n")
    
    choice = input(">> ")
    
    if choice.strip() == '1':
        click_mode = 'left'
    elif choice.strip() == '2':
        click_mode = 'right'
    elif choice.strip() == '3':
        click_mode = 'both'
    else:
        print("Invalid choice. Defaulting to left auto click.")
        click_mode = 'left'

get_click_mode()

click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

with Listener(on_click=on_click) as listener:
    listener.join()