from Utils.singleton_driver import BrowserSingleton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Alert:
    def __init__(self):
        self.alert = WebDriverWait(BrowserSingleton().driver, 10).until(EC.alert_is_present())

    def get_text(self):
        return self.alert.text

    def close_alert(self):
        self.alert.accept()

    def dismiss(self):
        self.alert.dismiss()

    def send_keys(self, text):
        self.alert.send_keys(text)