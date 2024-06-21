from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.button import Button


class MainPage(BasePage):
    __UNIQUE_ELEMENT = '//*[contains(@class, "banner-image")]'
    __ALERT_BUTTON = '//*[contains(@class, "card-body")]//*[contains(text(), "Alerts")]'
    __ELEMENS_BUTTON = '//*[contains(@class, "card-body")]//*[contains(text(), "Elements")]'

    def __init__(self):
        super().__init__(By.XPATH, self.__UNIQUE_ELEMENT, 'Main page')

    def push_alerts_frame_and_windows(self):
        Button(By.XPATH, self.__ALERT_BUTTON, 'Alerts').wait_and_click()

    def push_tables_button(self):
        Button(By.XPATH, self.__ELEMENS_BUTTON, 'Elements').wait_and_click()
