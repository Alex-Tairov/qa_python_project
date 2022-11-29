import time
import random

from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from locators.elements_page_locators import RadioButtonPageLocators
from locators.elements_page_locators import WebPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person
from selenium.webdriver.common.by import By

class TextBoxPage(BasePage):
    locators=TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_button = self.element_is_visible(self.locators.SUBMIT)
        self.driver.execute_script("arguments[0].click();", submit_button)
        return full_name,email,current_address,permanent_address

    def check_filled_form(self):
        full_name=self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email=self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address=self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address=self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return  full_name,email,current_address,permanent_address

class CheckBoxPage(BasePage):
    locators=CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list=self.element_are_visible(self.locators.ITEM_LIST)
        count=21
        while count!=0:
            item=item_list[random.randint(1,15)]
            if count>0:
                self.go_to_element(item)
                item.click()
                count-=1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list=self.element_are_visible(self.locators.CHEKED_ITEMS)
        data=[]
        for box in checked_list:
            title_item=box.find_element(By.XPATH,self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self,choice):
        choices={'Yes':self.locators.YES_RADIOBUTTON,
                'Impressive':self.locators.IMPRESSIVE_RADIOBUTTON,
                'No':self.locators.NO_RADIOBUTTON}
        radio=self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablePage(BasePage):
    locators = WebPageLocators()

    def add_new_person(self):
        count=1
        while count!=0:
            person_info=next(generated_person())
            first_name=person_info.first_name
            last_name=person_info.last_name
            email=person_info.email
            age=person_info.age
            salary=person_info.salary
            department=person_info.department
            self.element_is_visible(self.locators.ADD_USER_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count-=1
            return [first_name,last_name,str(age),email,str(salary),department]

    def check_new_added_person(self):
        people_list=self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data=[]
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self,key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_searched_person(self):
        delete_button=self.element_is_present(self.locators.DELETE_BUTTON)
        row=delete_button.find_element(By.XPATH,self.locators.ROW_PARENT)
        return row.text.splitlines()


















