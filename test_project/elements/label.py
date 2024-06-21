from elements.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, search_strategy, locator, name):
        super().__init__(search_strategy, locator, name)