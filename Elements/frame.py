from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.singleton_driver import BrowserSingleton
from Utils.logger import Logger


logger = Logger().logger


class FrameExtractor:
    def __init__(self):
        self.driver = BrowserSingleton().driver

    def get_text_from_frame(self):
        logger.info(f'Wait to be located Main Frame')
        parent_frame = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'frame1'))
        )

        logger.info(f'Switch to Parent Frame')
        self.driver.switch_to.frame(parent_frame)

        logger.info(f'Get text from Parent Frame')
        parent_frame_text = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Parent frame")]'))
        ).text

        logger.info(f'Wait to be located Child Frame')
        child_frame = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(@srcdoc, "Child Iframe")]'))
        ) 

        logger.info(f'Switch to Child Frame')
        self.driver.switch_to.frame(child_frame)

        logger.info(f'Get text from Child Frame')
        child_frame_text = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Child Iframe")]'))
        ).text

        logger.info(f'Go out from Frames')
        self.driver.switch_to.default_content()
        
        return parent_frame_text, child_frame_text
