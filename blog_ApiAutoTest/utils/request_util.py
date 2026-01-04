import requests


class Request:
    def get(self,url,**kwargs):
        print("准备发起get请求，url:" + url)
        print("接口信息：{}".format(**kwargs))

        r = requests.get(url=url,**kwargs)

        print("响应状态码：{}".format(r.status_code))
        print("响应内容：{}".format(r.json()))
        return r