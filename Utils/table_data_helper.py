from Pages.main_page import MainPage
from Forms.webtables_form import WebTablesForm
from Utils.json_helper import JsonHelper
from Utils.singleton_driver import BrowserSingleton


def get_all_data():
    main_page = MainPage()
    main_page.push_tables_button()
    web_table_page = WebTablesForm()
    web_table_page.click_webtables_button()
    web_table_page.get_table_elements()
    data = JsonHelper().read_json('Test_data/users_info.json')
    BrowserSingleton().quit_driver()
    return data


def get_data_range():
    return range(len(get_all_data()))