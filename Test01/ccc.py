from pywinauto import Application
from pywinauto.timings import wait_until

# app = Application(backend="uia").connect(process=12028)
# win = app.window(title_re=".*te.*")
# # win.print_control_identifiers()
# win.wait("visible")
# win.minimize()
# win.child_window(title="还原", control_type="Button")
# win.maximize()


# app = Application(backend="uia").connect(process=28572)
# win = app.window(title="计算器")

# win.print_control_identifiers()

# # 未启用的按钮
# btn1 = win.child_window(title="清除所有记忆", auto_id="ClearMemoryButton", control_type="Button")
# btn1.wait_not("enabled")
#
# # 启用的按钮
# btn2 = win.child_window(title="记忆加法", auto_id="MemPlus", control_type="Button")
# btn2.wait("enabled")

# # ready:启用且可见  visible + enabled
# btn = win.child_window(title="打开导航", auto_id="TogglePaneButton", control_type="Button")
# print(btn.is_visible())
# print(btn.is_enabled())
# btn.wait("ready")       #成功
#
# text = win.child_window(auto_id="PaneTitleTextBlock", control_type="Text")
# text.wait("exists")
# print(text.is_visible())
# print(text.is_enabled())
# text.wait("ready")      #失败

# 对控件进行操作后进入active状态
# btn = win.child_window(title="一", auto_id="num1Button", control_type="Button")
# btn.click_input()

# 对控件设置focus
# btn.set_focus()
# btn.wait("active")

# 对窗口设置focus
# win.set_focus()
# win.wait("active")

# i = 0
# def work():
#     global i
#     i += 1
#     print("i的值为:",i)
#     return i
#
# # 在5秒以内 每隔0.1秒调用函数 直到value=10  如果5秒以内到不了 则报错超时
# wait_until(5,0.1,work,value=10)

def get_window():
    app = Application(backend="uia").connect(process=28572)
    win = app.window(title="计算器")
    return win.is_visible()

# 等待到控件可见
wait_until(5,0.5,get_window,True)