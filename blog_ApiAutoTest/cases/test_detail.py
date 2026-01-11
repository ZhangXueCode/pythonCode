import pytest
from jsonschema.validators import validate

from utils.request_util import host, Request
from utils.yaml_util import read_yml


class TestDetail:
    url = host + "blog/getBlogDetail"
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
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "id",
                    "title",
                    "content",
                    "userId",
                    "deleteFlag",
                    "createTime",
                    "updateTime",
                    "loginUser"
                ],
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    },
                    "userId": {
                        "type": "integer"
                    },
                    "deleteFlag": {
                        "type": "integer"
                    },
                    "createTime": {
                        "type": "string"
                    },
                    "updateTime": {
                        "type": "string"
                    },
                    "loginUser": {
                        "type": "boolean"
                    }
                }
            }
        }
    }

    def test_detail_nologin(self):
        url = self.url + "?blogId=123"
        r = Request().get(url=url)
        assert r.status_code == 401

    def test_detail_login(self):
        url = self.url + "?blogId=" + str(read_yml("data.yml", "blogId"))
        token = read_yml("data.yml", "user_token_header")
        header = {
            "user_token_header": token
        }
        r = Request().get(url=url, headers=header)

        validate(r.json(), self.schema)

        assert r.json()["code"] == "SUCCESS"

    # 异常登录
    @pytest.mark.parametrize("blogId", ["", 1, -1, "比特", 10000000000])
    def test_detail_fail(self, blogId):
        url = self.url
        param = {
            "blogId": blogId
        }
        token = read_yml("data.yml", "user_token_header")
        header = {
            "user_token_header": token
        }
        r = Request().get(url=url, headers=header,params=param)

        expect_json = {
            "code": "FAIL",
            "errMsg": "内部错误, 请联系管理员",
            "data": None
        }

        assert r.json() == expect_json
