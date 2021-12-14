import pynput
import os

class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
@CallingCounter
def adjustBack():
    c=adjustBack.count
    if c%2==0:
       c=int(c)
       print(c)

def on_click(x, y, button, pressed):
    if str(button) == "Button.right":
        adjustBack()



with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
