import time

import win32con
import win32gui
import os
def window_enumeration_handler(hwnd,i):
     dirpath = os.getcwd() + "\start.exe"
     if win32gui.GetWindowText(hwnd) == "start.exe - 快捷方式" or win32gui.GetWindowText(hwnd) == dirpath or win32gui.GetWindowText(hwnd) == "start":
         win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
time.sleep(6)
win32gui.EnumWindows(window_enumeration_handler,0)
