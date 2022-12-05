import random
import time

from locators.interactions_page_locators import DroppablePageLocators
from pages.base_page import BasePage

class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    def drop_revert_draggable(self, type_drag):
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT, },
            'not_will':
                {'revert': self.locators.NOT_REVERT},
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert