import requests

from utils.logger_util import logger

host = "http://47.108.157.13:8090/"

class Request:
    log = logger.getLog()
    def get(self,url,**kwargs):
        self.log.info("准备发起get请求，url:" + url)
        self.log.info("接口信息：{}".format(kwargs))

        r = requests.get(url=url,**kwargs)

        self.log.info("响应状态码：{}".format(r.status_code))
        self.log.info("响应内容：{}".format(r.json()))
        return r

    def post(self,url,**kwargs):
        self.log.info("准备发起post请求，url:" + url)
        self.log.info("接口信息：{}".format(kwargs))

        r = requests.post(url=url,**kwargs)

        self.log.info("响应状态码：{}".format(r.status_code))
        self.log.info("响应内容：{}".format(r.json()))
        return r
