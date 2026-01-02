import pytest

# 按照文件执行
# @pytest.fixture(scope="module")
# def op():
#     print("初始化")
#     yield
#     print("清理")

# 按照会话执行  设置autouse=True可以不显示传op方法名
# @pytest.fixture(scope="session",autouse=True)
# def op():
#     print("初始化")
#     yield
#     print("清理")