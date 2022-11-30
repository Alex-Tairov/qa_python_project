import random
import time

from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage
from pages.elements_page import WebTablePage
from pages.elements_page import ButtonsPage
from pages.elements_page import LinksPage,UploadAndDownloadPage,DynamicPropertiesPage

class TestElements:
    class TestTextBox:
        def test_text_box(self,driver):
            text_box_page=TextBoxPage(driver,'https://demoqa.com/text-box')
            text_box_page.open()
            full_name,email,current_address,permanent_address=text_box_page.fill_all_fields()
            output_name,output_email,output_cur_address,output_per_address = text_box_page.check_filled_form()
            assert full_name==output_name,"the full name does not match"
            assert email==output_email,"the email does not match"
            assert current_address==output_cur_address,"the current_address does not match"
            assert permanent_address==output_per_address,"the permanent_address does not match"

    class TestCheckBox:
        def test_check_box(self,driver):
            check_box_page=CheckBoxPage(driver,'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox=check_box_page.get_checked_checkboxes()
            output_checkbox=check_box_page.get_output_result()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox==output_checkbox,"checkbox does not matchfi"

    class TestRadioButton:
        def test_radio_button(self,driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('Yes')
            output_yes=radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('No')
            output_no = radio_button_page.get_output_result()
            assert output_yes=='Yes',"'Yes' have not been selected"
            assert output_impressive=='Impressive',"'Impressive' have not been selected"
            assert output_no=='No',"'No' have not been selected"

    class TestWebTable:
        def test_web_table_add_person(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person=web_table_page.add_new_person()
            table_result=web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_table_search_person(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word=web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_some_person(key_word)
            table_result=web_table_page.check_searched_person()
            assert key_word in table_result,"the person wasn't found in the table"

        def test_table_update_person_info(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_searched_person()
            print(age)
            print(row)
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed or has changed incorrectly'

        class TestButtonsPage:
            def test_different_click_on_the_buttons(self, driver):
                buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
                buttons_page.open()
                double=buttons_page.click_on_double_button()
                right=buttons_page.click_on_right_button()
                click=buttons_page.click_on_click_me_button()
                assert double == "You have done a double click", "The double click button was not pressed"
                assert right == "You have done a right click", "The right click button was not pressed"
                assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

        class TestLinksPage:
            def test_check_link(self,driver):
                links_page=LinksPage(driver,'https://demoqa.com/links')
                links_page.open()
                response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
                assert response_code == 400, "the link works or the status code in son 400"

            def test_broken_link(self,driver):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
                assert response_code == 400, "the link works or the status code in son 400"

        class TestUploadAndDownload:
            def test_upload_file(self, driver):
                upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
                upload_download_page.open()
                file_name,result=upload_download_page.upload_file()
                assert file_name == result, "the file has not been uploaded"

            def test_download_file(self, driver):
                upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
                upload_download_page.open()
                upload_download_page.download_file()
                check = upload_download_page.download_file()
                assert check is True, "the file has not been downloade"

        class TestDynamicPropertiesPage:

            def test_dynamic_properties(self, driver):
                dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open()
                color_before, color_after = dynamic_properties_page.check_changed_of_color()
                assert color_after != color_before, 'colors have not been changed'

            def test_appear_button(self, driver):
                dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open()
                appear = dynamic_properties_page.check_appear_of_button()
                assert appear is True, 'button did not appear after 5 second'

            def test_enable_button(self, driver):
                dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open()
                enable = dynamic_properties_page.check_enable_button()
                assert enable is True, 'button did not enable after 5 second'













