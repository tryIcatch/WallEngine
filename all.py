from win32gui import GetWindowText, FindWindow
import win32gui

def window_enumeration_handler(hwnd, videoname):
     if GetWindowText(hwnd)== videoname:
        return hwnd
def pretreatmentHandle():
    hwnd = FindWindow("Progman", "Program Manager")
    win32gui.SendMessageTimeout(hwnd, 0x052C, 0, None, 0, 0x03E8)
    hwnd_WorkW = None
    while 1:
        hwnd_WorkW = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
        # print('hwmd_workw: ', hwnd_WorkW)
        if not hwnd_WorkW:
            continue
        hView = win32gui.FindWindowEx(hwnd_WorkW, None, "SHELLDLL_DefView", None)
        # print('hwmd_hView: ', hView)
        if not hView:
            continue
        h = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
        # print('h_1: ',h)
        while h:
            win32gui.SendMessage(h, 0x0010, 0, 0)  # WM_CLOSE
            h = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
            # print(h)
        break
    return hwnd


h = win32gui.FindWindow(("Progman"), ("Program Manager"))
video_h =FindWindow(0, r".\video\video.mp4")
pretreatmentHandle()
win32gui.SetParent(video_h,h)

