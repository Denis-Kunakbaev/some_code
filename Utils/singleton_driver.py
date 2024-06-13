from Utils.singleton_meta import SingletonMeta
from Utils.browser_factory import WebDriverFactory



class BrowserSingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.driver = WebDriverFactory().get_webdriver()

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()
        SingletonMeta._instances = {}