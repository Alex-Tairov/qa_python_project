import random
import time
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators

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


