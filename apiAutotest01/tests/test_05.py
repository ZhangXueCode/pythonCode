import pytest

# 每个方法执行前执行
# @pytest.fixture(scope="function")
# def op():
#     print("初始化")
#     yield
#     print("清理")
#
# class Test:
#     def test01(self,op):
#         print("执行test01")
#
#     def test02(self,op):
#         print("执行test02")

# 每个类执行前执行
@pytest.fixture(scope="class")
def op():
    print("初始化")
    yield
    print("清理")

class aTest:
    def test01(self, op):
        print("执行test01")

    def test02(self, op):
        print("执行test02")

class bTest1:
    def test01(self, op):
        print("执行test01")

    def test02(self, op):
        print("执行test02")