from Elements.button import Button


class BasePage():
    def __init__(self, page_locator):
        self._page_locator = page_locator

    def is_opened(self):
        unique_element = Button(self._page_locator).find_element()
        return unique_element.is_displayed()
