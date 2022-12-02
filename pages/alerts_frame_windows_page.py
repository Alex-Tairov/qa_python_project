import random
import time
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators,AlertsPageLocators,FramesPageLocators,\
    NestedFramesPageLocators

from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()
    def check_window_buttons(self,button_name):
        if button_name=="new tab":
            locator=self.locators.NEW_TAB_BUTTON
        elif button_name=="new window":
            locator=self.locators.NEW_WINDOW_BUTTON
        self.element_is_visible(locator).click()
        self.select_handle(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):
    locators=AlertsPageLocators()
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result

class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def text_frame(self,locator_frame,locator_text):
        frame = self.element_is_present(locator_frame)
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(locator_text).text
        return text

    def check_nested_frame(self):
        parent_text=self.text_frame(self.locators.PARENT_FRAME,self.locators.PARENT_TEXT)
        child_text=self.text_frame(self.locators.CHILD_FRAME,self.locators.CHILD_TEXT)
        return parent_text, child_text


