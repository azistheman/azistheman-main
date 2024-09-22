from pynput.mouse import Button, Controller, Listener
import time
import threading

mouse = Controller()
click_interval = 0.1
auto_clicking = False
click_mode = 'left'

def choose_click_speed():
    global click_interval
    print("\nEnter desired speed:")
    print("**cps may be vary due to prossesing speed**\n")

    print("[1] ~10cps")
    print("[2] ~20cps")
    print("[3] ~50cps")
    print("[4] ~100cps\n")

    click_speed = input(">> ")

    if click_speed == '1':
        click_interval = 0.1
    elif click_speed == '2':
        click_interval = 0.05
    elif click_speed == '3':
        click_interval = 0.02
    elif click_speed == '4':
        click_interval = 0.01
    else:
        print("Invalid choice. Defaulting to ~10cps.")
        click_interval = 0.1

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

get_click_mode()
choose_click_speed()

click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

with Listener(on_click=on_click) as listener:
    listener.join()