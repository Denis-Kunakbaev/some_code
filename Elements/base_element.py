from Utils.singleton_driver import BrowserSingleton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, locator):
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return BrowserSingleton().driver.find_element(By.XPATH, self.locator)

    def wait_and_click(self):
        button = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator))
            )
        button.click()

    def wait_for_displayed(self):
        element = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator))
            )
        return element.is_displayed()
    
    def wait_and_send_text(self, text):
        element = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.locator))
            )
        element.send_keys(text)

    def wait_and_get_text(self):
        text = WebDriverWait(BrowserSingleton().driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.locator))
            ).text
        return text
    
    def send_keys(self, text):
        self.find_element().send_keys(text)

