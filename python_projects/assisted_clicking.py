from pynput.mouse import Button, Controller, Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import time
import threading

mouse = Controller()
click_interval = 0.1
auto_clicking = False
click_mode = 'left'
stop_program = False  # Flag to stop the program

def clicker(click_count):
    global stop_program, auto_clicking
    while not stop_program:  # Loop until stop_program is set to True
        if auto_clicking:
            if click_mode == 'left':
                mouse.click(Button.left, click_count)
            elif click_mode == 'right':
                mouse.click(Button.right, click_count)
            elif click_mode == 'both':
                mouse.click(Button.left, click_count)
                mouse.click(Button.right, click_count)
            time.sleep(click_interval)

def on_click(x, y, button, pressed):
    global auto_clicking
    if button == Button.left:
        if pressed:
            auto_clicking = True
        else:
            auto_clicking = False

def on_key_press(key):
    global stop_program
    if hasattr(key, 'char') and key.char == '=':  # If the `=` key is pressed
        stop_program = True  # Stop the program
        print("Stopping the program...")

def get_click_mode():
    global click_mode
    print("\nChoose your click mode (default is left):\n")
    print("[1] Left")
    print("[2] Right")
    print("[3] Left & Right\n")
    
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

# Get click mode
get_click_mode()

# Get click count and validate input
while True:
    try:
        print("\nChoose assisted click amount ")
        print("(higher number more cpu usage):\n")
        
        x = int(input(">>"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Start the auto-clicking thread
click_thread = threading.Thread(target=clicker, args=(x,))
click_thread.daemon = True
click_thread.start()

# Start the mouse and keyboard listeners
with MouseListener(on_click=on_click) as mouse_listener, KeyboardListener(on_press=on_key_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()
