import requests
import pytest


def divide(a, b):
    assert b != 0, "除数不能为0"
    return a / b


def atest():
    print(divide(10, 2))
    print(divide(1, 0))


def btest():
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    r = requests.get(url)
    assert r.json()[0]["id"] == 1


def ctest():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    r = requests.get(url)
    expect = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    actual = r.json()
    assert expect == actual


def dtest():
    url = "https://jsonplaceholder.typicode.com/"
    r = requests.get(url)
    text = "Use your own data"
    assert text in r.text


@pytest.mark.parametrize("data", [1, 2, "a"])
def etest(data):
    print(data)


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
def ftest(n, expected):
    assert (n + 1) == expected


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
def gtest1(n, expected):
    assert (n * 1) + 1 == expected

# 作用在类上
@pytest.mark.parametrize("data", (1, 2, "a"))
class aTest:
    def test(self, data):
        print(data)

# 作用在全局
# pytestmark = pytest.mark.parametrize("data", (1, 2, "a"))
class bTest:
    def test(self, data):
        print(data)

class cTest1:
    def test(self,data):
        print(data)

# 自定义参数
def a():
    return [1,2,3]

@pytest.mark.parametrize("data",a())
def htest(data):
    print(data)