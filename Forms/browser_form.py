from Forms.base_form import BaseForm
from Elements.button import Button
from Elements.text_field import TextField
from Elements.tabs import TabElement

class BrowserForm(BaseForm):
    def __init__(self):
        super().__init__('//*[contains(text(), "New Tab")]')

    def click_new_tab_button(self):
        Button('//*[contains(text(), "New Tab")]').wait_and_click()
        TabElement().switch_to_new_tab()

    def get_text_from_new_tab(self):
        text = TextField('//*[contains(@id, "sampleHeading")]').wait_and_get_text()
        return text
    
    def close_current_tab(self):
        TabElement().close_tab()
        TabElement().switch_to_start_tab()

    def click_to_links(self):
        Button('//*[contains(@class, "element-group")]//*[contains(text(), "Elements")]').wait_and_click()
        Button('//*[contains(@id, "item-5")]//*[contains(text(), "Links")]').wait_and_click()