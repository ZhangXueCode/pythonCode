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

def test(d,e):
    assert d in e
