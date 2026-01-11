import re

import pytest
from jsonschema.validators import validate

from utils.request_util import host, Request
from utils.yaml_util import write_yml

@pytest.mark.order(1)
class TestLogin:
    url = host + "user/login"
    schema = {
        "type": "object",
        "required": ["code", "errMsg", "data"],
        "additionalProperties": False,
        "properties": {
            "code": {
                "type": "string"
            },
            "errMsg": {
                "type": "string"
            },
            "data": {
                "type": ["string", "null"]
            }
        }
    }

    @pytest.mark.parametrize("login", [
        # 错误的用户名
        {
            "username": "zhang",
            "password": "123456",
            "errMsg": "用户不存在"
        },
        # 错误的密码
        {
            "username": "zhangsan",
            "password": "1234",
            "errMsg": "密码错误"
        },
        # 全错误
        {
            "username": "zhang",
            "password": "1234",
            "errMsg": "用户不存在"
        },
        # 不存在
        {
            "username": "xxxx",
            "password": "qqqq",
            "errMsg": "用户不存在"
        },
        # 为空
        {
            "username": "",
            "password": "",
            "errMsg": "账号或密码不能为空"
        }])
    def test_login_fail(self, login):
        data = {
            "username": login["username"],
            "password": login["password"]
        }
        rq = Request()
        r = rq.post(url=self.url, data=data)

        validate(instance=r.json(), schema=self.schema)

        assert r.json()["code"] == "FAIL"
        assert r.json()["errMsg"] == login["errMsg"]

    @pytest.mark.parametrize("login", [
        {
            "username": "zhangsan",
            "password": "123456"

        },
        {
            "username": "lisi",
            "password": "123456"

        }])
    def test_login_successful(self, login):
        data = {
            "username": login["username"],
            "password": login["password"]
        }
        r = Request().post(url=self.url, data=data)

        validate(instance=r.json(), schema=self.schema)

        assert r.json()["code"] == "SUCCESS"
        assert re.match('\S{100,}', r.json()['data'])

        token = {
            "user_token_header": r.json()["data"]
        }

        write_yml("data.yml",token)
