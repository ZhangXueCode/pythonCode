import requests

get = requests.get("https://www.baidu.com")
print("get:", get)
print(get.text)
