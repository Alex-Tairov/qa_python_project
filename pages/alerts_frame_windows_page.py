import random
import time
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators,AlertsPageLocators

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


