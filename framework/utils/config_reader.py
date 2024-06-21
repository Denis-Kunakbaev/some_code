from utils.json_helper import JsonHelper
from utils.singleton_meta import SingletonMeta


class ConfigReader(metaclass=SingletonMeta):
    __BROWSER_SETTINGS_PATH = 'configs/settings.json'

    def __init__(self):
        self._config = self.read_config()

    def read_config(self):
        return JsonHelper(self.__BROWSER_SETTINGS_PATH).get_data()

    def get_config(self):
        SingletonMeta.clear_instances()
        return self._config
