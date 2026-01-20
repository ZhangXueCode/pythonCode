from pywinauto import Application
from pywinauto.keyboard import send_keys

# send_keys("12345")

# app = Application(backend="uia").connect(process=23344)
# win = app.window(title_re=".*te.*")
# win.wait("visible")

# win.type_keys("123")
# win.type_keys("hello{SPACE 2}world")

# ctrl -> ^
# shift -> +
# alt -> %

# win.type_keys("^a{BACKSPACE}")   #全选＋删除
# win.type_keys("+9hello{SPACE 3}world+0")  #（hello   world）
# win.type_keys("{ENTER}hello{ENTER}world")
# win.type_keys("1{+}2=3")  #{+}防止加号被转义为shift键