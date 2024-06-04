#coding:utf-8
import win32con
import win32api
import time
import pyperclip

Keyboardcodes = '''aA 65
bB 66
cC 67
dD 68
eE 69
fF 70
gG 71
hH 72
iI 73
jJ 74
kK 75
lL 76
mM 77
nN 78
oO 79
pP 80
qQ 81
rR 82
sS 83
tT 84
uU 85
vV 86
wW 87
xX 88
yY 89
zZ 90
0) 48
1! 49
2@ 50
3# 51
4$ 52
5% 53
6^ 54
7& 55
8* 56
9( 57
;: 186
=+ 187
,< 188
-_ 189
.> 190
/? 191
`~ 192
[{ 219
\| 220
]} 221
'" 222'''
Keyboardcode = {}
Keyboardcode[' '] = [1, 32]
for i in Keyboardcodes.split('\n'):
    key, vaule = i.split(' ')
    vaule = int(vaule)
    Keyboardcode[key[0]] = [1, vaule]
    Keyboardcode[key[1]] = [2, vaule]


def start(text):
    #第一个参数，键盘对应数字，查表
    #第二个，第四个没用
    #第三个参数，0代表按下，win32con.KEYEVENTF_KEYUP松开
    for line in text.split('\r\n'):
        for i in line:
            j = Keyboardcode.get(i)
            if j == None:
                pass
            elif j[0] == 1:
                win32api.keybd_event(j[1], 0, 0, 0)
                win32api.keybd_event(j[1], 0, win32con.KEYEVENTF_KEYUP, 0)
            elif j[0] == 2:
                win32api.keybd_event(16, 0, 0, 0)
                win32api.keybd_event(j[1], 0, 0, 0)
                win32api.keybd_event(j[1], 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.2)


# 获取当前剪切板内容
clipboard_content = pyperclip.paste()
print("当前剪切板内容:", clipboard_content)
print('等待3s后开始打印剪切板内容')
time.sleep(3)
start(clipboard_content)
print('打印完成')
