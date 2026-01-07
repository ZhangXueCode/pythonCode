import re

import pytest
from jsonschema.validators import validate

from utils.request_util import host, Request


class TestLogin:
    url = host + "user/login"
    schema = {
        "type": "object",
        "required": ["code", "errMsg", "data"],
        "additionalProperties":False,
        "properties": {
            "code": {
                "type": "string"
            },
            "errMsg": {
                "type": "string"
            },
            "data": {
                "type": ["string","null"]
            }
        }
    }

    @pytest.mark.parametrize("login",[
        {
            "name":"zhangsan",
            "password":"123456"

    },
        {
            "name": "lisi",
            "password": "123456"

    }])
    def test_login_successful(self,login):
        data = {
            "name": login["name"],
            "password": login["password"]
        }
        rq = Request()
        r = rq.post(url=self.url, data=data)

        validate(instance=r.json(),schema=self.schema)

        assert r.json()["code"] == "SUCCESS"
        assert re.match("/S{100,}",r.json()["data"])
