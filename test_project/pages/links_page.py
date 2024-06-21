from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.browser import Browser
from elements.button import Button


class LinksPage(BasePage):
    def __init__(self):
        super().__init__(By.XPATH, '//*[contains(@id, "no-content")]', 'Links form')

    def click_home_link(self):
        Button(By.XPATH, '//*[contains(@id,"simpleLink")]', 'Home').wait_and_click()

    def switch_to_new_tab(self):
        Browser().switch_to_new_tab()

    def switch_back(self):
        Browser().switch_to_start_tab()