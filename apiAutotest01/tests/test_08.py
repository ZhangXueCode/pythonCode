import pytest

# 用fixture传参
# @pytest.fixture(params=[1,2,3])
# def op(request):
#     return request.param
#
# def atest(op):
#     print(op)

def p():
    return [1,2,3]

@pytest.fixture(params=p())
def a(request):
    return request.param

def atest(a):
    print(a)