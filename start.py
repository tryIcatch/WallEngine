import os
import threading
import time
from multiprocessing import Process

def hide(i):
    os.system("hide.exe")
def StartVideo(i):
      os.system("OpenVideo.exe")
def SET(i):
    os.system("SET.exe")



t=threading.Thread(target=StartVideo,args=(1,))
t.start()
t.join(6)
t1=threading.Thread(target=SET,args=(1,))
t1.start()
t1.join(7)
t2=threading.Thread(target=hide,args=(1,))
t2.start()
t2.join(8)