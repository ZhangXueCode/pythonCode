import json

import yaml

# 写入yml文件
def write_yml(file,data):
    with open(file,"a+",encoding="utf8") as f:
        yaml.safe_dump(data,f)

# 读yml文件
def read_yml(file):
    with open(file,"r",encoding="utf8") as f:
        ret = yaml.safe_load(f)
        return json.dumps(ret)

# 清空文件
def clear(file):
    with open(file,"w",encoding="utf8") as f:
        f.truncate()



# 测试写入yml文件
# def test():
#     data = {
#         "name" : "zhangsan",
#         "age" : 12
#     }
#     write_yml("test.yml",data)


# 测试读yml文件
# def test():
#     r = read_yml("test.yml")
#     print(r)

# 测试清空文件
def atest():
    clear("test.yml")