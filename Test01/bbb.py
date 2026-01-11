import time

from pywinauto import Application

app = Application(backend="uia").connect(process=31680)
win = app.window(title_re=".*te.*")
win.wait("visible")

# win.close()

# 判断是否是顶级窗口
print(win.is_dialog())

# 将窗口最大化
win.maximize()
print(win.is_maximized())
print(win.get_show_state())  #1

time.sleep(2)

# 还原窗口初始大小
win.restore()
print(win.is_normal())
print(win.get_show_state())  #0

time.sleep(2)

# 将窗口最小化
win.minimize()
print(win.is_minimized())
print(win.get_show_state())  #2
