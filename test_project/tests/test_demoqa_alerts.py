from pages.main_page import MainPage
from pages.alerts_page import AlertsPage
from utils.logger import Logger as logger
import pytest


@pytest.mark.usefixtures('browser')
class TestAlerts:
    def test_alerts(self):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), 'The main page did not open'

        main_page.push_alerts_frame_and_windows()
        alerts_page = AlertsPage()
        alerts_page.click_alerts_button()
        logger.info('Alerts page must be opened')
        assert alerts_page.is_opened()

        alerts_page.click_to_see_alert()
        logger.info('Checking that the texts match')
        assert alerts_page.get_alert_text() == 'You clicked a button'
        
        alerts_page.close_alert()
        alerts_page.click_confirm_box()
        logger.info('Checking that the texts match')
        assert alerts_page.get_confirm_text() == 'Do you confirm action?'

        logger.info('Checking resul is OK')
        assert alerts_page.get_confirm_result() == 'You selected Ok'

        alerts_page.click_promt_box()
        logger.info('Checking that the texts match')
        assert f'You entered {alerts_page.type_word()}' == alerts_page.get_promt_result()
