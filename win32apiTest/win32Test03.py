# coding=utf-8
'''
自动登录QQ的程序
'''
__author__ = 'wtj'

import win32gui
import win32api
import win32con
from ctypes import *
from ctypes.wintypes import BOOL, HWND, LPARAM
from comtypes import COMError
from comtypes.automation import VARIANT
from comtypes.client import GetModule
import winreg  #window regedit  api
import  subprocess
user32 = windll.LoadLibrary("user32")


def getWindowClass(hwnd, buf=create_string_buffer(1024)):
    size = sizeof(buf)
    user32.GetClassNameA(hwnd, buf, size)
    return buf.value.strip()


def getWindowText(hwnd, buf=create_string_buffer(1024)):
    len = win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH) + 1
    print(len)
    win32gui.SendMessage(
        hwnd, win32con.WM_GETTEXT, len, buf)
    return buf.value.strip()


def print_text(hwnd, extra):
    _dighwnd = win32gui.GetDlgItem(hwnd, 0)
    print(_dighwnd)


@WINFUNCTYPE(BOOL, HWND, LPARAM)  # python和c 
def print_title(hwnd, extra):
    title = create_string_buffer(1024)
    user32.GetWindowTextA(hwnd, title, 255)
    title = title.value
    if title.decode('latin-1') == "QQ":
        print('###hwnd=%d,title=%s' % (hwnd, title))
        _point=win32gui.GetCursorPos()#当前鼠标位置
        _mouseHwnd=win32gui.WindowFromPoint(_point)#当前鼠标的句柄
        if(_mouseHwnd!=hwnd):
        	print('当前不是qq界面')
        else:
        	print('当前qq界面')
        	#TODO

    return 1
    #找到qq目录运行qq.exe
def startQQ():
    key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\\Tencent\\bugReport\\QQ',0,winreg.KEY_READ)
    value=winreg.QueryValueEx(key,'InstallDir')
    print(value[0])#D:\QQ\
    _path=value[0]+'\\\Bin\\QQ.exe' #D:\QQ\Bin
    subprocess.Popen(_path,shell=True)
    winreg.CloseKey(key)



if __name__ == '__main__':
    startQQ()
    # user32.EnumWindows(print_title, 0)
