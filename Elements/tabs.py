from Utils.singleton_driver import BrowserSingleton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TabElement:
    def __init__(self):
        self.driver = BrowserSingleton().driver

    def switch_to_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def switch_to_start_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])

    def close_tab(self):
        self.driver.close()


