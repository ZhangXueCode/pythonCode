import time

from pywinauto import Application

# app = Application(backend="uia").connect(process=28572)
# win = app.window(title="计算器")
# win.wait("visible")
#
# # win.print_control_identifiers()
#
# btn_1 = win.child_window(title="一", auto_id="num1Button", control_type="Button")
# btn_1.click_input()
# btn_1.wait("visible")
# time.sleep(2)
#
# btn_2 = win.child_window(title="加", auto_id="plusButton", control_type="Button")
# btn_2.click_input()
# btn_2.wait("visible")
# time.sleep(2)
#
# btn_3 = win.child_window(title="二", auto_id="num2Button", control_type="Button")
# btn_3.click_input()
# btn_3.wait("visible")
# time.sleep(2)
#
# btn_4 = win.child_window(title="等于", auto_id="equalButton", control_type="Button")
# btn_4.click_input()
# btn_4.wait("visible")
# time.sleep(2)

app = Application(backend="uia").connect(process=27688)
win = app.window(class_name_re=".*te.*")
win.wait("visible")

# win.print_control_identifiers()

# best_match
# pro = win['Menu1']
#
# for item in pro.children():
#     item.click_input()
#     time.sleep(2)

# win.right_click_input()

# print(win.texts())
# print(win.window_text())

# pro = win. child_window(title="添加新标签页", auto_id="AddButton", control_type="Button")
# print(pro.texts())
# print(pro.window_text())


