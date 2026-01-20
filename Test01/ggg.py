import os.path
import time

from pywinauto import Application, mouse

# 微信自动发送信息

# app = Application(backend="uia").connect(process=11672)
# win = app.window(title="微信文件传输助手网页版 - Google Chrome")
# win.wait("visible")
#
# # win.print_control_identifiers()
#
# btn = win['Edit1']
# btn.click_input()
# win.type_keys("hello")
# btn2 = win.child_window(title="发送",control_type="Hyperlink")
# btn2.click_input()

app = Application(backend="uia").connect(process=23344)
win = app.window(title_re=".*te.*")
win.wait("exists")

# win.print_control_identifiers()

# menu = win["Menu"]

# menu.print_control_identifiers()
# print(menu.children())
# print("----------------------------------")
# print(menu.items())
# print("----------------------------------")
# print(menu.item_by_index(0))

# save = menu.item_by_path("文件 -> 保存")
# point = save.rectangle().mid_point()
# # save.click_input()
# mouse.move(coords=(point.x,point.y))


# 自动创建文件
# for i in range(1,5):
#     win.type_keys("第一个文件^s")
#     save_win = win.child_window(title="另存为",control_type="Window")
#     filename = f"D:\\file\\text_{i}.txt"
#     save_win.child_window(title="文件名:",control_type="Edit").type_keys(filename)
#     save_win.child_window(title="保存(S)",control_type="Button").click_input()
#     time.sleep(2)
#     assert os.path.exists(filename)
#     win.type_keys("^n")


