from Elements.base_element import BaseElement


class TextField(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)