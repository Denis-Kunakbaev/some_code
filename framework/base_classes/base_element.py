from utils.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger as logger
from utils.config_reader import ConfigReader


class BaseElement:
    __WAITING_TIME = ConfigReader().get_config()['waiting_time']

    def __init__(self, search_strategy, locator, name):
        self.search_strategy = search_strategy
        self.locator = locator
        self.name = name

    def click(self):
        logger.info(f'Click to {self.name}')
        self.find_element().click()

    def find_element(self):
        logger.info(f'Try to find {self.name}')
        return Browser()._driver.find_element(self.search_strategy, self.locator)

    def wait_and_click(self):
        logger.info(f'Wait for be clickable and click {self.name}')
        button = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
            EC.element_to_be_clickable((self.search_strategy, self.locator))
            )
        button.click()

    def is_displayed_after_wait(self):
        logger.info(f'Wait for be displayed and click {self.name}')
        element = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
            EC.visibility_of_element_located((self.search_strategy, self.locator))
            )
        return element.is_displayed()

    def wait_and_send_text(self, text):
        logger.info(f'Wait for be clickable and send text {self.name}')
        element = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
            EC.element_to_be_clickable((self.search_strategy, self.locator))
            )
        element.send_keys(text)

    def wait_and_get_text(self):
        logger.info(f'Wait for be located and get text from {self.name}')
        text = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
            EC.presence_of_element_located((self.search_strategy, self.locator))
            ).text
        return text

    def send_keys(self, text):
        logger.info(f'Find {self.name} and send text')
        self.find_element().send_keys(text)

    def make_clickable_and_click(self):
        element = Browser()._driver.find_element(self.search_strategy, self.locator)
        Browser()._driver.execute_script("arguments[0].click();", element)
