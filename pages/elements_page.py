import time
import allure
import random
import base64
import requests
import os
from locators.elements_page_locators import LinksPageLocators,UploadAndDownloadPageLocators,DynamicPropertiesPageLocators,\
    TextBoxPageLocators,CheckBoxPageLocators,RadioButtonPageLocators,WebPageLocators,ButtonsPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person,generated_file
from selenium.webdriver.common.by import By

class TextBoxPage(BasePage):
    locators=TextBoxPageLocators()

    @allure.step("Fill in all fields")
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

    @allure.step('check filled form')
    def check_filled_form(self):
        full_name=self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email=self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address=self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address=self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return  full_name,email,current_address,permanent_address

class CheckBoxPage(BasePage):
    locators=CheckBoxPageLocators()

    @allure.step('open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('click random items')
    def click_random_checkbox(self):
        item_list=self.elements_are_visible(self.locators.ITEM_LIST)
        count=21
        while count!=0:
            item=item_list[random.randint(1,15)]
            if count>0:
                self.go_to_element(item)
                item.click()
                count-=1
            else:
                break

    @allure.step('get checked checkbox')
    def get_checked_checkboxes(self):
        checked_list=self.element_are_visible(self.locators.CHEKED_ITEMS)
        data=[]
        for box in checked_list:
            title_item=box.find_element(By.XPATH,self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('get output result')
    def get_output_result(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('click on the radiobutton')
    def click_on_the_radio_button(self,choice):
        choices={'Yes':self.locators.YES_RADIOBUTTON,
                'Impressive':self.locators.IMPRESSIVE_RADIOBUTTON,
                'No':self.locators.NO_RADIOBUTTON}
        radio=self.element_is_visible(choices[choice]).click()

    @allure.step('get output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablePage(BasePage):
    locators = WebPageLocators()

    @allure.step('add new person')
    def add_new_person(self):
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
        return [first_name,last_name,str(age),email,str(salary),department]

    @allure.step('check added people')
    def check_new_added_person(self):
        people_list=self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data=[]
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('find some person')
    def search_some_person(self,key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('check found person')
    def check_searched_person(self):
        delete_button=self.element_is_present(self.locators.DELETE_BUTTON)
        row=delete_button.find_element(By.XPATH,self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('update person information')
    def update_person_info(self):
        person_info=next(generated_person())
        age=person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step('delete person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('check count rows')
    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

class ButtonsPage(BasePage):
    locators=ButtonsPageLocators()

    @allure.step('click on double button')
    def click_on_double_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

    @allure.step('check right button')
    def click_on_right_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

    @allure.step('check click_me button')
    def click_on_click_me_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locators=LinksPageLocators()

    @allure.step('check simple link')
    def check_new_tab_simple(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step('check broken link')
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code

class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    @allure.step('upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('download file')
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\Admin\Desktop\Python\qa_python_project\filetest{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step('check enable button')
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('check changed of color')
    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('check appear of button')
    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True

























