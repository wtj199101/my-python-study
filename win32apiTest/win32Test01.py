# coding=utf-8
'''
这是测试程序
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
user32 = windll.LoadLibrary("user32")
# 得到window classname类名


def getWindowClass(hwnd, buf=create_string_buffer(1024)):
    size = sizeof(buf)
    user32.GetClassNameA(hwnd, buf, size)
    return buf.value.strip()


def getWindowText(hwnd, buf=create_string_buffer(1024)):
    # size = sizeof(buf)
    len = win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH) + 1
    print(len)
    win32gui.SendMessage(
        hwnd, win32con.WM_GETTEXT, len, buf)
    return buf.value.strip()


def print_text(hwnd, extra):
    _dighwnd = win32gui.GetDlgItem(hwnd, 0)
    print(_dighwnd)


@WINFUNCTYPE(BOOL, HWND, LPARAM)  # python和c 不能直接调用必须转为WNDENUMPROC类型通过ctype调用
def print_title(hwnd, extra):
    title = create_string_buffer(1024)
    user32.GetWindowTextA(hwnd, title, 255)
    title = title.value
    # print(title.decode('latin-1') )
    # print(title.decode('latin-1'))
    if title.decode('latin-1') == "QQ":
        print('###hwnd=%d,title=%s' % (hwnd, title))
        _point=win32gui.GetCursorPos()#当前鼠标位置
        _mouseHwnd=win32gui.WindowFromPoint(_point)#当前鼠标的句柄
        if(_mouseHwnd!=hwnd):
        	print('当前不是qq界面')
        else:
        	print('当前qq界面')
        	#TODO
 # _pycwnd = win32gui.FindWindowEx(hwnd, None, None, None)
 # self.iObjectId = iObjectId
# print(_pycwnd)
# print(IAccessible)
# print(iObjectId)
# 920088 [985874][65552]
# print(title)
# user32.GetWindowTextA(hwnd,title,255)
# print(title)
# digName = getWindowClass(hwnd)
# print(digName)
# _digText = getWindowText(hwnd)
# print(digName)
# dlg = win32gui.FindWindowEx(hwnd, None, 'Edit', None)
# print(dlg)
# print(getWindowText(dlg))
# # print(_pycwnd)
# # win32gui.EnumChildWindows(_pycwnd, print_text, None)
# btnhld = win32gui.FindWindowEx(hwnd, None,'Button', None)
# print(btnhld)
    return 1

if __name__ == '__main__':
    # 鼠标移动上去得到窗口句柄
    # winCurPos=win32api.GetCursorPos()#得到鼠标的光标
    # print(winCurPos)
    # Hwnd=win32gui.WindowFromPoint(winCurPos)
    # print(Hwnd)
    # winCur=win32gui.FindWindowEx(Hwnd,None,None,None)
    # print(winCur)
    user32.EnumWindows(print_title, 0)
