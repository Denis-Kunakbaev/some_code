from Utils.browser_singleton_meta import BrowserSingletonMeta
from Utils.browser_factory import WebDriverFactory


class BrowserSingleton(metaclass=BrowserSingletonMeta):
    def __init__(self):
        self.driver = WebDriverFactory().get_webdriver()

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()
        self.driver = None
