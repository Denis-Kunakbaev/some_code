from utils.singleton_meta import SingletonMeta
import logging


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler('Logs/logfile.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    @staticmethod
    def debug(message):
        Logger().logger.debug(message)

    @staticmethod
    def info(message):
        Logger().logger.info(message)

    @staticmethod
    def warning(message):
        Logger().logger.warning(message)

    @staticmethod
    def error(message):
        Logger().logger.error(message)

    @staticmethod
    def critical(message):
        Logger().logger.critical(message)
