from Forms.base_form import BaseForm
from Elements.button import Button
from Elements.alert import Alert
from Elements.text_field import TextField
from Elements.frame import FrameExtractor
import random
import string


class AlertsForm(BaseForm):
    def __init__(self):
        super().__init__('//*[contains(@id, "item-1")] //*[contains(text(), "Alerts")]')

    def click_alerts_button(self):
        Button('//*[contains(@id, "item-1")] //*[contains(text(), "Alerts")]').wait_and_click()

    def click_nested_frames_button(self):
        Button('//*[contains(text(), "Nested Frames")]').wait_and_click()

    def check_nested_frame_is_open(self):
        parent_frame_text = FrameExtractor().get_text_from_frame()[0]
        child_frame_text = FrameExtractor().get_text_from_frame()[1]
        return parent_frame_text, child_frame_text
    
    def click_frame_button(self):
        Button('//*[@id="item-2"]//*[contains(text(), "Frames")]').wait_and_click()

    def get_text_from_frames(self):
        frame_1_text = TextField('//*[contains(@id, "frame1Wrapper")]').wait_and_get_text()
        frame_2_text = TextField('//*[contains(@id, "frame2Wrapper")]').wait_and_get_text()
        return (frame_1_text, frame_2_text)

    def click_to_see_alert(self):
        button = Button('//*[@id="alertButton"]')
        button.wait_and_click()

    def click_confirm_box(self):
        Button('//*[@id="confirmButton"]').wait_and_click()
    
    def get_confirm_text(self):
        alert = Alert()
        text = alert.get_text()
        alert.close_alert()
        return text

    def get_confirm_result(self):
        confirm_text = TextField('//*[@id="confirmResult"]').wait_and_get_text()
        return confirm_text

    def click_promt_box(self):
        Button('//*[@id="promtButton"]').wait_and_click()

    def get_promt_result(self):
        return TextField('//*[@id="promptResult"]').wait_and_get_text()

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
        Button('//*[@id="item-0"]//*[contains(text(), "Browser")]').wait_and_click()


