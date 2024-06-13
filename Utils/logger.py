from Utils.singleton_meta import SingletonMeta
import logging


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler('Logs/logfile.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

