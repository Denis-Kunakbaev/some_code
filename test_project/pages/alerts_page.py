from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.button import Button
from utils.string_helper import StringHelper
from elements.text_field import TextField
from utils.browser import Browser


class AlertsPage(BasePage):
    __ALERT_BUTTON = '//*[contains(@id, "item-1")] //*[contains(text(), "Alerts")]'
    __NESTED_FRAMES_BUTTON = '//*[contains(text(), "Nested Frames")]'
    __SHOW_ALERT_BUTTON = '//*[contains(@id, "alertButton")]'
    __CONFIRM_BUTTON = '//*[contains(@id, "confirmButton")]'
    __CONFIRM_BOX = '//*[contains(@id, "confirmResult")]'
    __PROMT_BUTTON = '//*[contains(@id, "promtButton")]'
    __PROMT_RESULT = '//*[contains(@id, "promptResult")]'
    __BROWSER_BUTTON = '//*[contains(@id, "item-0")]//*[contains(text(), "Browser")]'
    __RANDOM_STRING_LENGTH = 8

    def __init__(self):
        super().__init__(By.XPATH, self.__ALERT_BUTTON, 'Alerts form')

    def click_alerts_button(self):
        Button(By.XPATH, self.__ALERT_BUTTON, 'Alerts button').wait_and_click()

    def click_nested_frames_button(self):
        Button(By.XPATH, self.__NESTED_FRAMES_BUTTON, 'Nested Frames').wait_and_click()

    def click_to_see_alert(self):
        button = Button(By.XPATH, self.__SHOW_ALERT_BUTTON, 'See alert')
        button.wait_and_click()

    def click_confirm_box(self):
        Button(By.XPATH, self.__CONFIRM_BUTTON, 'Confirm button').wait_and_click()

    def get_confirm_text(self):
        text = self.get_alert_text()
        Browser().close_alert()
        return text

    def get_confirm_result(self):
        confirm_text = TextField(By.XPATH, self.__CONFIRM_BOX, 'Confirm box').wait_and_get_text()
        return confirm_text

    def click_promt_box(self):
        Button(By.XPATH, self.__PROMT_BUTTON, 'Promt box').wait_and_click()

    def get_promt_result(self):
        return TextField(By.XPATH, self.__PROMT_RESULT, 'Promt box').wait_and_get_text()

    def get_alert_text(self):
        return Browser().get_alert().text

    def close_alert(self):
        Browser().close_alert()

    def type_word(self):
        alert = Browser().get_alert()
        random_string = StringHelper().get_random_string(self.__RANDOM_STRING_LENGTH)
        alert.send_keys(random_string)
        self.close_alert()
        return random_string

    def click_browser_button(self):
        Button(By.XPATH, self.__BROWSER_BUTTON, 'Browser Windows').wait_and_click()
