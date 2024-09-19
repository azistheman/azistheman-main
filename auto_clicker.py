from pynput.mouse import Button, Controller
import time
print ("running")
go=2
mouse = Controller()
run=True

while run==True:
    time.sleep(5)
    go=3
    mouse.click(Button.left, 10000000)
    
    run=False