from lib2to3.pygram import pattern_grammar

import requests
from jsonschema import validate


def atest():
    json_data = {
        "code": "SUCCESS",
        "errMsg": "",
        "data": False
    }
    json_schema = {
        "type": "object",
        "required": [],
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
    validate(json_data, json_schema)


def btest():
    url = "http://47.108.157.13:8090/blog/getList"
    head = {
        "user_token_header": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlck5hbWUiOiJ6aGFuZ3NhbiIsImV4cCI6MTc2NzM2NTIxOX0.CvuPW7z3Tfc3JsrbunroO2rLJvEA3E7C737ffRK1US8"
    }
    r = requests.get(url, headers=head)
    json_schema = {
        "type": "object",
        "required": [],
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
                    "required": [],
                    "properties": {
                        "id": {
                            "type": "number"
                        },
                        "title": {
                            "type": "string"
                        },
                        "content": {
                            "type": "string"
                        },
                        "userId": {
                            "type": "number"
                        },
                        "deleteFlag": {
                            "type": "number"
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
    validate(r.json(), json_schema)


# 限制数组里的元素
def ctest():
    json = {
        "a": [1, 2, 3, 4, 5]
    }

    json_schema = {
        "type": "object",
        "properties": {
            "a": {
                "type": "array",
                "minItems": 1,
                "maxItems": 5,
                "uniqueItems": True,
                "items": {
                    "type": "number"
                }
            }
        }
    }
    validate(json, json_schema)

# 对字符串的限制
def dtest():
    json = {
        "name": "zhangsan",
        "age": 12
    }
    json_schema = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                # 个数至少为12个
                "pattern":"/S{12,}"
            },
            "age": {
                "type": "number"
            }
        }
    }

# 对象约束
def etest():
    json = {
        "name": "zhangsan",
        "age": 12,
        "aaa":"aaa"
    }

    json_schema = {
        "type": "object",
        # 默认为True 表示允许schema中没有的元素存在
        "additionalProperties":"False",
        "properties": {
            "name": {
                "type": "string",
            },
            "age": {
                "type": "number"
            }
        }
    }

# 必须属性
def ftest():
    json = {
        "name": "zhangsan",
        "age": 12,
        "aaa": "aaa"
    }

    json_schema = {
        "type": "object",
        # 表示json中必须返回name这个属性
        "required":["name"],
        "properties": {
            "name": {
                "type": "string",
            },
            "age": {
                "type": "number"
            }
        }
    }

# 依赖关系
def gtest():
    json = {
        "name": "zhangsan",
        "age": 12,
        "aaa": "aaa"
    }

    json_schema = {
        "type": "object",
        # 表示返回age则必须返回aaa
        "dependentRequired":{
            "age":["aaa"]
        },
        "properties": {
            "name": {
                "type": "string",
            },
            "age": {
                "type": "number"
            }
        }
    }

