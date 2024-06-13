from Pages.base_page import BasePage
from Elements.button import Button


class MainPage(BasePage):
    def __init__(self):
        super().__init__('//*[@class="banner-image"]')

    def push_alerts_frame_and_windows(self):
        Button('//*[contains(@class, "card-body")]//*[contains(text(), "Alerts")]').wait_and_click()

    def push_tables_button(self):
        Button('//*[contains(@class, "card-body")]//*[contains(text(), "Elements")]').wait_and_click()