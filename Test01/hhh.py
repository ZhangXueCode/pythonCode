
from datetime import datetime

from pywinauto import Application, mouse
#
# app = Application(backend="uia").connect(process=12024)
# win = app.window(title_re=".*文件资源管理器.*")
# win.wait("exists")
#
# btn = win.child_window(control_type="List",auto_id="HomeListView")
# print(btn.get_items())

# print(len(btn.get_items()))
# print(btn.item_count())

# btn.get_item(row=2).double_click_input()

# for i in btn.get_items():
#     point = i.rectangle().mid_point()
#     mouse.move(coords=(point.x,point.y))
#     time.sleep(1)

# app = Application(backend="uia").connect(process=1460)
# win = app.window(title="微信文件传输助手网页版 - Google Chrome")
# win.wait("visible")

# win.print_control_identifiers()

# message_b = win.child_window(control_type="List")
# len_b = message_b.item_count()
#
# edit = win["Edit2"]
# edit.click_input()
# message = "比特-" + str(datetime.now())
# edit.type_keys(message,with_spaces=True)
# send = win.child_window(title="发送",control_type="Hyperlink")
# send.click_input()
#
# message_l = win.child_window(control_type="List")
# len_l = message_l.item_count()
#
# assert message == message_l.get_item(row=len_l - 1).window_text()
# assert len_b + 1 == len_l or len_b + 2 == len_l