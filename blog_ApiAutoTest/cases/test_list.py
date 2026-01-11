import pytest
from jsonschema.validators import validate

from utils.request_util import host, Request
from utils.yaml_util import read_yml, write_yml

@pytest.mark.order(2)
class TestList:
    url = host + "blog/getList"
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
                "type": "array",
                "items": {
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
    }


    def test_list_noLogin(self):
        r = Request().get(url=self.url)
        assert r.status_code == 401

    def test_list_login(self):
        token = read_yml("data.yml","user_token_header")
        header = {
            "user_token_header": token
        }
        r = Request().get(url=self.url,headers=header)

        validate(r.json(),self.schema)

        assert r.json()["code"] == "SUCCESS"

        blogId = {
            "blogId": r.json()["data"][0]["id"]
        }

        write_yml("data.yml",blogId)






