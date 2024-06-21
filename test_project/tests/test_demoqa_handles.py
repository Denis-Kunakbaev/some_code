from pages.main_page import MainPage
from pages.alerts_page import AlertsPage
from pages.browser_page import BrowserPage
from pages.links_page import LinksPage
from utils.logger import Logger as logger
import pytest


@pytest.mark.usefixtures('browser')
class TestHandles:
    SAMPLE_TEXT = 'This is a sample page'

    def test_handles(self):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), 'The main page did not open'

        main_page.push_alerts_frame_and_windows()
        AlertsPage().click_browser_button()
        browser_page = BrowserPage()
        logger.info('Browser page must be opened')
        assert browser_page.is_opened(), 'The browser page did not open'

        browser_page.click_new_tab_button()
        logger.info('New tab must be opened')
        assert browser_page.get_text_from_new_tab() == self.SAMPLE_TEXT, 'The main page did not open'

        browser_page.close_current_tab()
        logger.info('New tab must be closed')
        assert browser_page.is_opened(), 'The browser page did not open'

        browser_page.click_to_links()
        links_page = LinksPage()
        logger.info('Links page must be opened')
        assert links_page.is_opened(), 'The Links page did not open'

        links_page.click_home_link()
        links_page.switch_to_new_tab()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), 'The main page did not open'

        links_page.switch_back()
        logger.info('Links page must be opened')
        assert links_page.is_opened(), 'The Links page did not open'