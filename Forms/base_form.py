from Elements.base_element import BaseElement
from Utils.logger import Logger


logger = Logger().logger


class BaseForm:
    def __init__(self, page_locator, name):
        self._page_locator = page_locator
        self._name = name

    def is_opened(self):
        logger.info(f'Check {self._name} is displayed')
        unique_element = BaseElement(self._page_locator, self._name).find_element()
        return unique_element.is_displayed()