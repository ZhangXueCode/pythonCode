import math
import time

from pywinauto import mouse, Application

# mouse.click(coords=(777,777))
# time.sleep(2)

# mouse.double_click(coords=(1210,38))

# mouse.right_click(coords=(1210,38))

# mouse.scroll(coords=(1410,786),wheel_dist=-2000)

# mouse.scroll(coords=(1410,786),wheel_dist=20000)

# app = Application(backend="uia").connect(process=27688)
# win = app.window(class_name_re=".*te.*")
# win.wait("visible")
#
# pro = win['Menu1']

# rect = pro.rectangle()
# print(rect)
# width = rect.right - rect.left
# height = rect.bottom - rect.top

# width = math.floor(width / 2) + rect.left
# height = math.floor(height / 2) + rect.top

# 获取到元组 里面对应正中间的坐标
# point = rect.mid_point()

# mouse.move(coords=(point.x,point.y))

# for i in pro.children():
#     point = i.rectangle().mid_point()
#     mouse.click(coords=(point.x,point.y))
#     time.sleep(2)

# 抖音刷赞
# app = Application(backend="uia").connect(title="抖音",timeout=10)
# win = app.window(title="抖音")
# win.wait("visible")
#
# for i in range(0,3):
#     point = win.rectangle().mid_point()
#     time.sleep(2)
#     # win.double_click_input()
#     mouse.double_click(coords=(point.x,point.y))
#     time.sleep(2)
#     mouse.scroll(coords=(point.x,point.y),wheel_dist=-500)

