from pages.main_page import MainPage
from pages.alerts_page import AlertsPage
from pages.frame_page import FramePage
from pages.nested_frame_page import NestedFramePage
from utils.logger import Logger as logger
import pytest
from utils.test_data_reader import TestDataReader


@pytest.mark.usefixtures('browser')
class TestFrame:
    _PARENT_FRAME, _CHILD_FRAME = TestDataReader().get_data()['frames'].values()

    def test_frame(self):
        main_page = MainPage()
        logger.info('Main page must be opened')
        assert main_page.is_opened(), 'The main page did not open'

        main_page.push_alerts_frame_and_windows()
        alerts_page = AlertsPage()
        alerts_page.click_nested_frames_button()
        logger.info('Checking that the texts in frames match')
        nested_frames_page = NestedFramePage()
        assert self._PARENT_FRAME in nested_frames_page.check_frame_is_open()[0] and self._CHILD_FRAME in nested_frames_page.check_frame_is_open()[1]

        nested_frames_page.click_frame_button()
        logger.info('Checking that the texts in frames match')
        frame_page = FramePage()
        assert frame_page.get_text_from_frames()[0] == frame_page.get_text_from_frames()[1]
