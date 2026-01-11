import os

import yaml


def write_yml(filename,data):
    with open(os.getcwd() + "/data/" + filename,mode="a+",encoding="utf8") as f:
        yaml.safe_dump(data,f)

def read_yml(filename,key):
    with open(os.getcwd() + "/data/" + filename, mode="r", encoding="utf8") as f:
        data = yaml.safe_load(f)
        return data[key]

def clear(filename):
    with open(os.getcwd() + "/data/" + filename, mode="w", encoding="utf8") as f:
        f.truncate()