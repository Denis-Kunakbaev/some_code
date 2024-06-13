from Utils.singleton_driver import BrowserSingleton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.logger import Logger


logger = Logger().logger


class BaseElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def click(self):
        logger.info(f'Click to {self.name}')
        self.find_element().click()

    def find_element(self):
        logger.info(f'Try to find {self.name}')
        return BrowserSingleton().driver.find_element(By.XPATH, self.locator)

    def wait_and_click(self):
        logger.info(f'Wait for be clickable and click {self.name}')
        button = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator))
            )
        button.click()

    def wait_for_displayed(self):
        logger.info(f'Wait for be displayed and click {self.name}')
        element = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator))
            )
        return element.is_displayed()
    
    def wait_and_send_text(self, text):
        logger.info(f'Wait for be clickable and send text {self.name}')
        element = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.locator))
            )
        element.send_keys(text)

    def wait_and_get_text(self):
        logger.info(f'Wait for be located and get text from {self.name}')
        text = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.locator))
            ).text
        return text
    
    def send_keys(self, text):
        logger.info(f'Find {self.name} and send text')
        self.find_element().send_keys(text)

