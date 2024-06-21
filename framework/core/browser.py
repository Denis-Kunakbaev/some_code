from utils.singleton_meta import SingletonMeta
from utils.browser_factory import WebDriverFactory
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger as logger
from utils.config_reader import ConfigReader


class Browser(metaclass=SingletonMeta):
    __WAITING_TIME = ConfigReader().get_config()['waiting_time']

    def __init__(self, browser_name):
        self._driver = None
        self._browser_name = browser_name
        self.URL = ConfigReader().get_config()['url']
        self.set_up_driver()

    def set_up_driver(self):
        self.options = WebDriverFactory.get_options(self._browser_name)
        if self._browser_name.lower() == WebDriverFactory.CHROME_NAME:
            self._driver = webdriver.Chrome(options=self.options)
        elif self._browser_name.lower() == WebDriverFactory.FF_NAME:
            self._driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=self.options)
        self._driver.get(self.URL)

    def get_driver(self):
        return self._driver

    def switch_to_new_tab(self):
        logger.info(f'Switch to New tab')
        tabs = self._driver.window_handles
        self._driver.switch_to.window(tabs[-1])

    def switch_to_start_tab(self):
        logger.info(f'Switch to Start tab')
        tabs = self._driver.window_handles
        self._driver.switch_to.window(tabs[0])

    def close_tab(self):
        logger.info(f'Close tab')
        self._driver.close()

    def quit_driver(self):
        self._driver.quit()
        SingletonMeta.clear_instances()

    def switch_to_frame(self, frame_name):
        logger.info(f'Switch to {frame_name}')
        self._driver.switch_to.frame(frame_name)

    def switch_to_default(self):
        logger.info(f'Go out from Frames')
        self._driver.switch_to.default_content()

    def get_alert(self):
        return WebDriverWait(self._driver, self.__WAITING_TIME).until(EC.alert_is_present())

    def close_alert(self):
        logger.info(f'Click to "OK" button on alert')
        self.get_alert().accept()

    def dismiss_alert(self):
        logger.info(f'Click to "Cancel" button on alert')
        self.get_alert().dismiss()