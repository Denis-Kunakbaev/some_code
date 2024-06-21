from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.text_field import TextField



class FramePage(BasePage):
    __PARENT_FRAME = '//*[contains(@id, "frame1Wrapper")]'
    __CHILD_FRAME = '//*[contains(@id, "frame2Wrapper")]'

    def __init__(self):
        super().__init__(By.XPATH, self.__PARENT_FRAME, 'Frame form')

    def get_text_from_frames(self):
        frame_1_text = TextField(By.XPATH, self.__PARENT_FRAME, 'Parent frame').wait_and_get_text()
        frame_2_text = TextField(By.XPATH, self.__CHILD_FRAME, 'Child frame').wait_and_get_text()
        return (frame_1_text, frame_2_text)
