from Utils.singleton_driver import BrowserSingleton
from Utils.logger import Logger


logger = Logger().logger


class TabElement:
    def __init__(self):
        self.driver = BrowserSingleton().driver

    def switch_to_new_tab(self):
        logger.info(f'Switch to New tab')
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def switch_to_start_tab(self):
        logger.info(f'Switch to Start tab')
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])

    def close_tab(self):
        logger.info(f'Close tab')
        self.driver.close()


