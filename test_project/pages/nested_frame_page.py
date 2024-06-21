from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader
from utils.browser import Browser
from utils.logger import Logger as logger
from elements.button import Button


class NestedFramePage(BasePage):
    __MAIN_FRAME = '//iframe[contains(@id, "frame1")]'
    __CHILD_FRAME = '//*[contains(@srcdoc, "Child Iframe")]'
    __PARENT_FRAME_TEXT = '//*[contains(text(), "Parent frame")]'
    __CHILD_FRAME_TEXT = '//*[contains(text(), "Child Iframe")]'
    __FRAMES_BUTTON = '//*[@id="item-2"]//*[contains(text(), "Frames")]'
    __WAITING_TIME = ConfigReader().get_config()['waiting_time']

    def __init__(self):
        super().__init__(By.XPATH, self.__MAIN_FRAME, 'Frame form')

    def click_frame_button(self):
        Button(By.XPATH, self.__FRAMES_BUTTON, 'Frames').wait_and_click()

    def check_frame_is_open(self):
        parent_frame_text = self.get_text_from_frame()[0]
        child_frame_text = self.get_text_from_frame()[1]
        return parent_frame_text, child_frame_text

    def get_text_from_frame(self):
        logger.info(f'Wait to be located Main Frame')
        parent_frame = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
        EC.presence_of_element_located((By.XPATH, self.__MAIN_FRAME))
        )

        logger.info(f'Switch to Parent Frame')
        Browser().switch_to_frame(parent_frame)

        logger.info(f'Get text from Parent Frame')
        parent_frame_text = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
        EC.presence_of_element_located((By.XPATH, self.__PARENT_FRAME_TEXT))
        ).text

        logger.info(f'Wait to be located Child Frame')
        child_frame = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
        EC.presence_of_element_located((By.XPATH, self.__CHILD_FRAME))
        ) 

        logger.info(f'Switch to Child Frame')
        Browser().switch_to_frame(child_frame)

        logger.info(f'Get text from Child Frame')
        child_frame_text = WebDriverWait(Browser()._driver, self.__WAITING_TIME).until(
        EC.presence_of_element_located((By.XPATH, self.__CHILD_FRAME_TEXT))
        ).text

        logger.info(f'Go out from Frames')
        Browser().switch_to_default()
        
        return parent_frame_text, child_frame_text
