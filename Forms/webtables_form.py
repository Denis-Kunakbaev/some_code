from Elements.button import Button
from Elements.table import Table
from Elements.text_field import TextField
from Forms.base_form import BaseForm
from Utils.json_helper import JsonHelper
from Utils.logger import Logger


logger = Logger().logger


class WebTablesForm(BaseForm):
    COLUMN_NAMES = ["firstName", "lastName", "age", "userEmail", "salary", "department"]
    DELETE_LOCATOR = '//*[contains(@id,"delete-record-")]'
    TABLE = '//*[contains(@id, "app")]//*[contains(@class, "rt-tbody")]'
    ADD_TO_TABLE = '//*[contains(@id, "addNewRecordButton")]'

    def __init__(self):
        super().__init__(self.ADD_TO_TABLE, 'Web tables form')

    def click_webtables_button(self):
        Button('//*[contains(text(), "Web Tables")]', 'Web tables').wait_and_click()

    def get_table_elements(self):
        table_rows = Table(self.TABLE, 'Users table').find_element()
        data = table_rows.text.rstrip().split('\n')
        num_columns = len(self.COLUMN_NAMES)
        users = [data[i:i + num_columns] for i in range(0, len(data), num_columns)]
        users_dict = [dict(zip(self.COLUMN_NAMES, user)) for user in users]
        JsonHelper.write_json('Test_data/users_info.json', users_dict)

    def get_length_of_table(self):
        table_rows = Table(self.TABLE, 'Users table').find_element()
        logger.info('Return table elements count')
        data = table_rows.text.rstrip().split('\n')
        return len(data)
    
    def delete_new_user(self):
        num_of_user = str(self.get_length_of_table() // 6)
        delete_locator = self.DELETE_LOCATOR.replace('delete-record-', 'delete-record-' + num_of_user)
        Button(delete_locator, 'Delete button').wait_and_click()
        logger.info('Delete user')
        
    def fill_registration_form(self, user):
        for key, value in user.items():
            TextField(key, key).wait_and_send_text(value)
        logger.info('Send user data to form')
        Button('//*[contains(@id, "submit")]', 'Submit user data').click()

    def click_add_button(self):
        Button(self.ADD_TO_TABLE, 'Add').wait_and_click()
        return TextField('//*[contains(@id,"registration-form-modal")]', 'Registartion form text').wait_for_displayed()
