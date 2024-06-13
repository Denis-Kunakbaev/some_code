from Elements.base_element import BaseElement


class BasePage():
    def __init__(self, page_locator, name):
        self._page_locator = page_locator
        self._name = name

    def is_opened(self):
        unique_element = BaseElement(self._page_locator, self._name).find_element()
        return unique_element.is_displayed()
