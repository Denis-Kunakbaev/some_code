from Pages.main_page import MainPage
from Forms.alerts_form import AlertsForm
from Forms.browser_form import BrowserForm
from Forms.webtables_form import WebTablesForm
from Forms.links_form import LinksForm
from Utils.table_data_helper import get_all_data
from Utils.logger import Logger
import pytest


logger = Logger().logger


class TestAlerts:
    MAIN_PAGE_WARNING = 'Главная страница не открылась'
    ALERT_TEXT = 'You clicked a button'
    CONFIRM_TEXT = 'Do you confirm action?'
    CONFIRM_RESULT = 'You selected Ok'

    def test_alerts(self):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), self.MAIN_PAGE_WARNING

        main_page.push_alerts_frame_and_windows()
        alerts_page = AlertsForm()
        alerts_page.click_alerts_button()
        logger.info('Alerts page must be opened')
        assert alerts_page.is_opened()

        alerts_page.click_to_see_alert()
        logger.info('Checking that the texts match')
        assert alerts_page.get_alert_text() == self.ALERT_TEXT
        
        alerts_page.close_alert()
        alerts_page.click_confirm_box()
        logger.info('Checking that the texts match')
        assert alerts_page.get_confirm_text() == self.CONFIRM_TEXT

        logger.info('Checking resul is OK')
        assert alerts_page.get_confirm_result() == self.CONFIRM_RESULT

        alerts_page.click_promt_box()
        logger.info('Checking that the texts match')
        assert f'You entered {alerts_page.type_word()}' == alerts_page.get_promt_result()

class TestFrame:
    MAIN_PAGE_WARNING = 'Главная страница не открылась'

    def test_frame(self):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), self.MAIN_PAGE_WARNING

        main_page.push_alerts_frame_and_windows()
        alerts_page = AlertsForm()
        alerts_page.click_nested_frames_button()
        logger.info('Checking that the texts in frames match')
        assert "Parent frame" in alerts_page.check_nested_frame_is_open()[0] and "Child Iframe" in alerts_page.check_nested_frame_is_open()[1]

        alerts_page.click_frame_button()
        logger.info('Checking that the texts in frames match')
        assert alerts_page.get_text_from_frames()[0] == alerts_page.get_text_from_frames()[1]


class TestTables:
    MAIN_PAGE_WARNING = 'Главная страница не открылась'
    WEB_TABLE_WARNING = 'Страница с web-таблицей не открылась'
    REGISTRATION_FORM = 'Форма регистрации не открылась'
    NEW_USER_DATA_WARNING = 'Данные пользователя не добавлены в таблицу'
    USER_IS_NOT_DELETED = 'Пользователь не был удален из таблицы'

    @pytest.mark.parametrize('user', get_all_data())
    def test_tables(self, user):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), self.MAIN_PAGE_WARNING

        main_page.push_tables_button()
        web_table_page = WebTablesForm()
        web_table_page.click_webtables_button()
        current_table = web_table_page.get_length_of_table()
        logger.info('Web table must be opened')
        assert web_table_page.is_opened(), self.WEB_TABLE_WARNING

        logger.info('Registration form must be opened')
        assert web_table_page.click_add_button(), self.REGISTRATION_FORM

        web_table_page.fill_registration_form(user)
        new_table = web_table_page.get_length_of_table()
        logger.info('New user must be added to table')
        assert current_table != new_table, self.NEW_USER_DATA_WARNING

        web_table_page.delete_new_user()
        current_table = web_table_page.get_length_of_table()
        logger.info('New user must be deleted to table')
        assert new_table != current_table, self.USER_IS_NOT_DELETED

class TestHandles:
    MAIN_PAGE_WARNING = 'Главная страница не открылась'
    SAMPLE_TEXT = 'This is a sample page'
    SAMPLE_PAGE_WARNING = 'Страница /sample не открылась'
    BROWSER_PAGE_WARNING = 'Страница Browser Windows не открылась'
    LINKS_PAGE_WARNING = 'Страница Links не открылась'

    def test_handles(self):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), self.MAIN_PAGE_WARNING

        main_page.push_alerts_frame_and_windows()
        AlertsForm().click_browser_button()
        browser_page = BrowserForm()
        logger.info('Browser page must be opened')
        assert browser_page.is_opened(), self.BROWSER_PAGE_WARNING

        browser_page.click_new_tab_button()
        logger.info('New tab must be opened')
        assert browser_page.get_text_from_new_tab() == self.SAMPLE_TEXT, self.MAIN_PAGE_WARNING

        browser_page.close_current_tab()
        logger.info('New tab must be closed')
        assert browser_page.is_opened(), self.BROWSER_PAGE_WARNING

        browser_page.click_to_links()
        links_page = LinksForm()
        logger.info('Links page must be opened')
        assert links_page.is_opened(), self.LINKS_PAGE_WARNING

        links_page.click_home_link()
        links_page.switch_to_new_tab()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), self.MAIN_PAGE_WARNING

        links_page.switch_back()
        logger.info('Links page must be opened')
        assert links_page.is_opened(), self.LINKS_PAGE_WARNING