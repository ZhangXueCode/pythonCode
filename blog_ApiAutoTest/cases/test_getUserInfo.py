from jsonschema.validators import validate

from utils.request_util import host, Request
from utils.yaml_util import read_yml


class TestgetUserInfo:
    url = host + "user/getUserInfo"
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

    def test_getUserInfo_nologin(self):
        r = Request().get(self.url)
        assert r.status_code == 401

    def test_getUserInfo(self):
        header = {
            "user_token_header": read_yml("data.yml", "user_token_header")
        }
        r = Request().get(self.url, headers=header)

        validate(r.json(),self.schema)

        assert r.json()["code"] == "SUCCESS"
