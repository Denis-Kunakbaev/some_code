from utils.json_helper import JsonHelper


class TestDataReader:
    __TEST_DATA_PATH = 'test_data/test_data.json'

    def __init__(self):
        self._data = self.read_data()

    def read_data(self):
        return JsonHelper(self.__TEST_DATA_PATH).get_data()

    def get_data(self):
        return self._data