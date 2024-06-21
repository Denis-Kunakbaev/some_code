from pages.main_page import MainPage
from pages.webtables_page import WebTablesPage
from utils.logger import Logger as logger
import pytest
from utils.test_data_reader import TestDataReader


users = TestDataReader().get_data()['users']


@pytest.mark.usefixtures('browser')
class TestTables:
    @pytest.mark.parametrize('user', users)
    def test_tables(self, user):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), 'The main page did not open'

        main_page.push_tables_button()
        web_table_page = WebTablesPage()
        web_table_page.click_webtables_button()
        current_table = web_table_page.get_length_of_table()
        logger.info('Web table must be opened')
        assert web_table_page.is_opened(), 'The web-table page did not open'

        logger.info('Registration form must be opened')
        assert web_table_page.click_add_button(), 'The registration form did not open'

        web_table_page.fill_registration_form(user)
        new_table = web_table_page.get_length_of_table()
        logger.info('New user must be added to table')
        assert current_table != new_table, 'New user details not added'

        web_table_page.delete_new_user()
        current_table = web_table_page.get_length_of_table()
        logger.info('New user must be deleted to table')
        assert new_table != current_table, 'The user was not removed from the table'
