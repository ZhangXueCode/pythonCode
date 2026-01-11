import pytest
from jsonschema.validators import validate

from utils.request_util import host, Request
from utils.yaml_util import read_yml


class TestAdd:
    url = host + "blog/add"
    schema = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "code",
            "errMsg",
            "data"
        ],
        "properties": {
            "code": {
                "type": "string"
            },
            "errMsg": {
                "type": "string"
            },
            "data": {
                "type": "boolean"
            }
        }
    }

    def test_add_nologin(self):
        r = Request().get(self.url)
        assert r.status_code == 401

    @pytest.mark.parametrize("add", [
        {
            "title": "接口自动化测试题目",
            "content": "接口自动化测试内容",
            "data":True
        },
        {
            "title": "",
            "content": "接口自动化测试内容",
            "data":False
        },
        {
            "title": "接口自动化测试题目",
            "content": "",
            "data":False
        },
        {
            "title": "",
            "content": "",
            "data":False
        },
        {
            "title":"带有图片",
            "content":"[![](https://cdn.pixabay.com/photo/2020/04/13/19/40/sun-5039871_1280.jpg)](https://cdn.pixabay.com/photo/2020/04/13/19/40/sun-5039871_1280.jpg)",
            "data":True
        },
        {
            "title": "链接",
            "content": "[百度](http://www.baidu.com \"百度\")",
            "data": True
        }
    ])
    def test_add_login(self, add):
        header = {
            "user_token_header": read_yml("data.yml", "user_token_header")
        }
        json = {
            "title": add["title"],
            "content": add["content"]
        }
        r = Request().post(self.url, headers=header,json=json)

        validate(r.json(),self.schema)

        assert r.json()["data"] == add["data"]
