from selenium.webdriver.common.by import By
from elements.button import Button
from elements.table import Table
from elements.text_field import TextField
from pages.base_page import BasePage
from utils.logger import Logger as logger


class WebTablesPage(BasePage):
    _COLUMN_NAMES = ["firstName", "lastName", "age", "userEmail", "salary", "department"]
    _DELETE_LOCATOR = '//*[contains(@id, "delete-record-")]'
    _TABLE = '//*[contains(@id, "app")]//*[contains(@class, "rt-tbody")]'
    _ADD_TO_TABLE = '//*[contains(@id, "addNewRecordButton")]'
    _WEB_TABLES_BUTTON = '//*[contains(text(), "Web Tables")]'
    _SUBMIT_BUTTON = '//*[contains(@id, "submit")]'
    _REGISTRATION_FORM_TEXT = '//*[contains(@id,"registration-form-modal")]'

    def __init__(self):
        super().__init__(By.XPATH, self._ADD_TO_TABLE, 'Web tables form')

    def click_webtables_button(self):
        Button(By.XPATH, self._WEB_TABLES_BUTTON, 'Web tables').wait_and_click()

    def get_length_of_table(self):
        table_rows = Table(By.XPATH, self._TABLE, 'Users table').find_element()
        logger.info('Return table elements count')
        data = table_rows.text.rstrip().split('\n')
        return len(data)
    
    def delete_new_user(self):
        user_id = self.get_length_of_table() // len(self._COLUMN_NAMES)
        delete_locator = self._DELETE_LOCATOR.replace('delete-record-', f'delete-record-{user_id}')
        Button(By.XPATH, delete_locator, 'Delete button').make_clickable_and_click()
        logger.info('Delete user')
        
    def fill_registration_form(self, user):
        for key, value in user.items():
            TextField(By.ID, key, key).wait_and_send_text(value)
        logger.info('Send user data to form')
        Button(By.XPATH, self._SUBMIT_BUTTON, 'Submit user data').click()

    def click_add_button(self):
        Button(By.XPATH, self._ADD_TO_TABLE, 'Add').wait_and_click()
        return TextField(By.XPATH, self._REGISTRATION_FORM_TEXT, 'Registartion form text').is_displayed_after_wait()
