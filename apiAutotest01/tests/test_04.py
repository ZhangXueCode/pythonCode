import pytest

@pytest.fixture
def a():
    return "a"

def atest(a):
    print(a)

# 嵌套
@pytest.fixture
def b():
    return "a"

@pytest.fixture
def c(b):
    return [b]

def btest(c):
    assert c == ["a"]

# 多个参数
class Fruit:
    def __init__(self,name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def d():
    return Fruit("apple")

@pytest.fixture
def e(d):
    return [Fruit("banana"),d]

def ctest(d,e):
    assert d in e

@pytest.fixture
def op():
    print("初始化")
    yield 100
    print("执行结束")

def dtest(op):
    print(100 + op)
    assert 100 == op

@pytest.fixture
def file_read():
    f = open("test.txt","r",encoding="utf8")
    yield f
    f.close()

@pytest.fixture
def file_write():
    f = open("test.txt","w",encoding="utf8")
    yield f

@pytest.fixture
def file_append():
    f = open("test.txt","a",encoding="utf8")
    yield f

def etest(file_write,file_append,file_read):
    w = file_write
    w.write("好工作")
    w.close()

    a = file_append
    a.write("难找")
    a.close()

    r = file_read
    print(r.read())