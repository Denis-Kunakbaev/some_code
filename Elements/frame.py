from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.singleton_driver import BrowserSingleton


class FrameExtractor:
    def __init__(self):
        self.driver = BrowserSingleton().driver

    def get_text_from_frame(self):
        parent_frame = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'frame1'))
        )
        self.driver.switch_to.frame(parent_frame)
        parent_frame_text = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Parent frame")]'))
        ).text
        child_frame = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(@srcdoc, "Child Iframe")]'))
        ) 
        self.driver.switch_to.frame(child_frame)
        child_frame_text = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Child Iframe")]'))
        ).text
        self.driver.switch_to.default_content()
        return parent_frame_text, child_frame_text
