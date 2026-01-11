import logging
import os.path
import time

class infoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

class errFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

class logger:
    @classmethod
    def getLog(cls):
        cls.logger = logging.getLogger(__name__)
        cls.logger.setLevel(logging.DEBUG)

        LOG_PATH = "./logs/"

        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)

        '''
        2026-1-1.log
        2026-1-1-info.log
        2026-1-1-err.log
        '''
        now = time.strftime("%Y-%m-%d")
        log_name = LOG_PATH + now + ".log"
        info_log_name = LOG_PATH + now + "-info.log"
        err_log_name = LOG_PATH + now + "-err.log"



        all_handler = logging.FileHandler(log_name,encoding="utf8")
        info_handler = logging.FileHandler(info_log_name,encoding="utf8")
        err_handler = logging.FileHandler(err_log_name,encoding="utf8")
        # 输出到控制台
        stream_handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s")

        all_handler.setFormatter(formatter)
        info_handler.setFormatter(formatter)
        err_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)


        info_handler.addFilter(infoFilter())
        err_handler.addFilter(errFilter())

        cls.logger.addHandler(all_handler)
        cls.logger.addHandler(info_handler)
        cls.logger.addHandler(err_handler)
        # cls.logger.addHandler(stream_handler)

        return cls.logger

