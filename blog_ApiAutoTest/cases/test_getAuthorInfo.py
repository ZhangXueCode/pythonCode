import pytest
from jsonschema.validators import validate

from utils.request_util import host, Request
from utils.yaml_util import read_yml


class TestgetAuthorInfo:
    url = host + "user/getAuthorInfo"
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
                    "userName",
                    "password",
                    "githubUrl",
                    "deleteFlag",
                    "createTime",
                    "updateTime"
                ],
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "userName": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    },
                    "githubUrl": {
                        "type": "string"
                    },
                    "deleteFlag": {
                        "type": "integer"
                    },
                    "createTime": {
                        "type": "string"
                    },
                    "updateTime": {
                        "type": "string"
                    }
                }
            }
        }
    }

    def test_getAuthorInfo_nologin(self):
        url = self.url + "?blogId=1"
        r = Request().get(url)
        assert r.status_code == 401

    def test_getAuthorInfo(self):
        url = self.url + "?blogId=" + str(read_yml("data.yml", "blogId"))
        header = {
            "user_token_header": read_yml("data.yml", "user_token_header")
        }
        r = Request().get(url, headers=header)

        validate(r.json(),self.schema)
        assert r.json()["code"] == "SUCCESS"

    @pytest.mark.parametrize("blogId,expect_code", [
        ("","FAIL"),
        (1,"FAIL"),
        (-1,"SUCCESS"),
        ("比特","FAIL"),
        (10000000000,"FAIL")
    ])
    def test_getAuthorInfo_fail(self,blogId,expect_code):
        url = self.url
        param = {
            "blogId": blogId
        }
        token = read_yml("data.yml", "user_token_header")
        header = {
            "user_token_header": token
        }
        r = Request().get(url=url, headers=header, params=param)

        assert r.json()["code"] == expect_code
