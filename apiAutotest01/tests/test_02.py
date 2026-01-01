# class Test:
#     # 在每个方法测试之前都会执行
#     def setup_method(self):
#         print("setup_method")
#
#     def test01(self):
#         print("test01")
#
#     def test02(self):
#         print("test02")
#
#     # 在每个方法测试之后都会执行
#     def teardown_method(self):
#         print("teardown_method")

class aTest:
    # 在所有方法测试之前执行
    def setup_class(self):
        print("setup_class")

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")

    # 在所有方法测试之后执行
    def teardown_class(self):
        print("teardown_class")