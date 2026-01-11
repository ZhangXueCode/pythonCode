import time

from pywinauto import Application

# 启动
# app = Application(backend="uia").start("notepad.exe")
# print(app.process)
# 连接
# Application(backend="uia").connect(process=app.process)

app = Application(backend="uia").connect(process=24800)

# 通过title
# win = app.window(title="无标题 - Notepad")

# 通过class_name
# win = app.window(class_name="Notepad")

# 通过title_re正则表达式
# win = app.window(title_re="无标题.*")

# 通过class_name_re正则表达式
# win = app.window(class_name_re=".*te.*")

# best_match的可选项
# ['无标题 - Notepad', 'Dialog', '无标题 - NotepadDialog', 'Dialog0', 'Dialog1']
# win = app.window(best_match='Dialog')


# 动态解析对象
# win = app.Dialog
# win = app["Dialog"]
# 有特殊符号或空格的只能用中括号括起来
# win = app['无标题 - NotepadDialog']

# 通过顶窗口找
win = app.top_window()


win.wait("visible")


# 打印控件相关信息
# win.print_control_identifiers()