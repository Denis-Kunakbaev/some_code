from elements.label import Label


class BasePage():
    def __init__(self, search_strategy, page_locator, name):
        self._page_locator = page_locator
        self._name = name
        self._search_strategy = search_strategy

    def is_opened(self):
        unique_element = Label(self._search_strategy, self._page_locator, self._name).find_element()
        return unique_element.is_displayed()
