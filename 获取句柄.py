from win32gui import FindWindowEx, ShowWindow, EnumWindows, GetWindowText, FindWindow

def window_enumeration_handler(hwnd,i):
            #if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            print(hwnd,GetWindowText(hwnd))
            pass

id=EnumWindows(window_enumeration_handler,0)
#print(id)
#x = FindWindow(0, r".\video\video.mp4")
#print(x)