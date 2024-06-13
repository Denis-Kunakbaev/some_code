from Utils.singleton_driver import BrowserSingleton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.logger import Logger


logger = Logger().logger


class Alert:
    def __init__(self):
        self.alert = WebDriverWait(BrowserSingleton().driver, 10).until(EC.alert_is_present())

    def get_text(self):
        logger.info(f'Get text from alert')
        return self.alert.text

    def close_alert(self):
        logger.info(f'Click to "OK" button on alert')
        self.alert.accept()

    def dismiss(self):
        logger.info(f'Click to "Cancel" button on alert')
        self.alert.dismiss()

    def send_keys(self, text):
        logger.info(f'Send to {text} to alert')
        self.alert.send_keys(text)