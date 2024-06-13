from Forms.base_form import BaseForm
from Elements.button import Button
from Elements.alert import Alert
from Elements.text_field import TextField
from Elements.frame import FrameExtractor
import random
import string
from Utils.logger import Logger


logger = Logger().logger


class AlertsForm(BaseForm):
    ALERT_BUTTON = '//*[contains(@id, "item-1")] //*[contains(text(), "Alerts")]'

    def __init__(self):
        super().__init__(self.ALERT_BUTTON, 'Alerts form')

    def click_alerts_button(self):
        Button(self.ALERT_BUTTON, 'Alerts button').wait_and_click()

    def click_nested_frames_button(self):
        Button('//*[contains(text(), "Nested Frames")]', 'Nested Frames').wait_and_click()

    def check_nested_frame_is_open(self):
        parent_frame_text = FrameExtractor().get_text_from_frame()[0]
        child_frame_text = FrameExtractor().get_text_from_frame()[1]
        return parent_frame_text, child_frame_text
    
    def click_frame_button(self):
        Button('//*[@id="item-2"]//*[contains(text(), "Frames")]', 'Frames').wait_and_click()

    def get_text_from_frames(self):
        frame_1_text = TextField('//*[contains(@id, "frame1Wrapper")]', 'Parent frame').wait_and_get_text()
        frame_2_text = TextField('//*[contains(@id, "frame2Wrapper")]', 'Child frame').wait_and_get_text()
        return (frame_1_text, frame_2_text)

    def click_to_see_alert(self):
        button = Button('//*[contains(@id, "alertButton")]', 'See alert')
        button.wait_and_click()

    def click_confirm_box(self):
        Button('//*[contains(@id, "confirmButton")]', 'Confirm button').wait_and_click()
    
    def get_confirm_text(self):
        alert = Alert()
        text = alert.get_text()
        alert.close_alert()
        return text

    def get_confirm_result(self):
        confirm_text = TextField('//*[contains(@id, "confirmResult")]', 'Confirm box').wait_and_get_text()
        return confirm_text

    def click_promt_box(self):
        Button('//*[contains(@id, "promtButton")]', 'Promt box').wait_and_click()

    def get_promt_result(self):
        return TextField('//*[contains(@id, "promptResult")]', 'Promt box').wait_and_get_text()

    def get_alert_text(self):
        alert = Alert()
        return alert.get_text()

    def close_alert(self):
        alert = Alert()
        alert.close_alert()

    def type_word(self):
        alert = Alert()
        random_string = ''.join(random.sample(set(string.ascii_letters), 8))
        alert.send_keys(random_string)
        alert.close_alert()
        return random_string
    
    def click_browser_button(self):
        Button('//*[contains(@id, "item-0")]//*[contains(text(), "Browser")]', 'Browser Windows').wait_and_click()


