from Pages.main_page import MainPage
from Forms.alerts_form import AlertsForm
from Forms.browser_form import BrowserForm
from Forms.webtables_form import WebTablesForm
from Forms.links_form import Links
from Utils.table_data_helper import get_all_data, get_data_range
import pytest



# class TestAlerts:
#     def test_alerts(self):
#         main_page = MainPage()
#         assert main_page.is_opened(), 'Главная страница не открылась'

#         main_page.push_alerts_frame_and_windows()
#         alerts_page = AlertsForm()
#         alerts_page.click_elements_button()
#         assert alerts_page.is_opened()

#         alerts_page.click_to_see_alert()
#         assert alerts_page.get_alert_text() == 'You clicked a button'
#         alerts_page.close_alert()

#         alerts_page.click_confirm_box()
#         assert alerts_page.get_confirm_text() == "Do you confirm action?"
#         assert alerts_page.get_confirm_result() == "You selected Ok"

#         alerts_page.click_promt_box()
#         assert f'You entered {alerts_page.type_word()}' == alerts_page.get_promt_result()

# class TestFrame:
#     def test_frame(self):
#         main_page = MainPage()
#         assert main_page.is_opened(), 'Главная страница не открылась'

#         main_page.push_alerts_frame_and_windows()
#         alerts_page = AlertsForm()
#         alerts_page.click_nested_frames_button()
#         assert "Parent frame" in alerts_page.check_nested_frame_is_open()[0] and "Child Iframe" in alerts_page.check_nested_frame_is_open()[1]

#         alerts_page.click_frame_button()
#         assert alerts_page.get_text_from_frames()[0] == alerts_page.get_text_from_frames()[1]


class TestTables:
    @pytest.fixture(scope='function', autouse=True)
    def user(self, request):
        return get_all_data()[request.param]

    @pytest.mark.parametrize('user', get_data_range())
    def test_tables(self, user):
        main_page = MainPage()
        assert main_page.is_opened(), 'Главная страница не открылась'
        main_page.push_tables_button()
        web_table_page = WebTablesForm()
        web_table_page.click_webtables_button()
        current_table = web_table_page.get_length_of_table()
        assert web_table_page.is_opened(), 'Страница с web-таблицей не открылась'
        assert web_table_page.click_add_button(), 'Форма регистрации не открылась'
        web_table_page.fill_registration_form(user)
        web_table_page.click_submit_button()
        new_table = web_table_page.get_length_of_table()
        assert current_table != new_table, 'Данные пользователя не добавлены в таблицу'
        web_table_page.delete_new_user()
        current_table = web_table_page.get_length_of_table()
        assert new_table != current_table, 'Пользователь не был удален из таблицы'

# class TestHandles:
#     SAMPLE_TEXT = 'This is a sample page'
#     def test_handles(self):
#         main_page = MainPage()
#         assert main_page.is_opened(), 'Главная страница не открылась'
#         main_page.push_alerts_frame_and_windows()
#         AlertsForm().click_browser_button()
#         browser_page = BrowserForm()
#         assert browser_page.is_opened(), 'Страница Browser Windows не открылась'
#         browser_page.click_new_tab_button()
#         assert browser_page.get_text_from_new_tab() == self.SAMPLE_TEXT, 'Страница /sample не открылась'
#         browser_page.close_current_tab()
#         assert browser_page.is_opened(), 'Страница Browser Windows не открылась'
#         browser_page.click_to_links()
#         links_page = Links()
#         assert links_page.is_opened(), 'Страница Links не открылась'
#         links_page.click_home_link()
#         links_page.switch_to_new_tab()
#         assert main_page.is_opened()
#         links_page.switch_back()
#         assert links_page.is_opened(), 'Страница Links не открылась'



