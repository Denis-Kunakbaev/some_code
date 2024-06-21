from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.button import Button
from elements.text_field import TextField
from utils.browser import Browser


class BrowserPage(BasePage):
    __BROWSER_FORM = '//*[contains(text(), "New Tab")]'
    __NEW_TAB_BUTTON = '//*[contains(text(), "New Tab")]'
    __NEW_TAB_TEXT = '//*[contains(@id, "sampleHeading")]'
    __ELEMENTS_BUTTON = '//*[contains(@class, "element-group")]//*[contains(text(), "Elements")]'
    __LINKS_BUTTON = '//*[contains(@id, "item-5")]//*[contains(text(), "Links")]'
    def __init__(self):
        super().__init__(By.XPATH, self.__BROWSER_FORM, 'Browser form')

    def click_new_tab_button(self):
        Button(By.XPATH, self.__NEW_TAB_BUTTON, 'New tab').wait_and_click()
        Browser().switch_to_new_tab()

    def get_text_from_new_tab(self):
        text = TextField(By.XPATH, self.__NEW_TAB_TEXT, 'New tab text').wait_and_get_text()
        return text
    
    def close_current_tab(self):
        Browser().close_tab()
        Browser().switch_to_start_tab()

    def click_to_links(self):
        Button(By.XPATH, self.__ELEMENTS_BUTTON, 'Elements').wait_and_click()
        Button(By.XPATH, self.__LINKS_BUTTON, 'Links').wait_and_click()