from Forms.base_form import BaseForm
from Elements.tabs import TabElement
from Elements.button import Button


class LinksForm(BaseForm):
    def __init__(self):
        super().__init__('//*[contains(@id, "no-content")]', 'Links form')

    def click_home_link(self):
        Button('//*[contains(@id,"simpleLink")]', 'Home').wait_and_click()

    def switch_to_new_tab(self):
        TabElement().switch_to_new_tab()

    def switch_back(self):
        TabElement().switch_to_start_tab()