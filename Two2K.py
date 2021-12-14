import time
import win32api
import os
import win32con
import threading

def StartVideo(w,h):
    os.system(fr".\Fplay\ffplay.exe  .\video\video.mp4 -noborder -x {w} -y {h} -loop 0  ")

w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
Videothreading = threading.Thread(target=StartVideo, args=(w, h))
Videothreading.start()
Videothreading.join(5)