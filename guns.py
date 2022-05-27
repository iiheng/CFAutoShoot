import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as kController
from pynput.keyboard import Key


s,r = 0,0
keyboard = kController()
mouse = Controller()
def snipe():
    global s
    s+=1
    keyboard.press(Key.shift)
    mouse.press(Button.right)
    time.sleep(0.01)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    mouse.release(Button.right)
    time.sleep(0.01)
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(0.2)
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(1)
    keyboard.release(Key.shift)
    print("snipe:"+str(s))

def rifle():
    global r
    r +=1
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    print('rifle:'+str(r))