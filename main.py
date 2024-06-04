import pyperclip
import pyautogui
import time

# 获取当前剪切板内容
clipboard_content = pyperclip.paste()
print("当前剪切板内容:", clipboard_content)
# 延时以确保你有时间切换到目标窗口
print('等待3s后开始打印剪切板内容')
time.sleep(3)
# 模拟键盘输出
pyautogui.typewrite(clipboard_content)
print('打印完成')
