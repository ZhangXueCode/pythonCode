import logging

logging.basicConfig(level=logging.INFO)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

logger = logging.getLogger("my_logger")

logger.setLevel(level=logging.DEBUG)

handler = logging.FileHandler(filename="test.log")

formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s")

# 将格式器设置到处理器上
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
