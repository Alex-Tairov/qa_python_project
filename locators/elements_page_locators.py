from selenium.webdriver.common.by import By

class TextBoxPageLocators:

   #form_fields
   FULL_NAME=(By.CSS_SELECTOR,"input[id='userName']")
   EMAIL=(By.CSS_SELECTOR,"input[id='userEmail']")
   CURRENT_ADDRESS=(By.CSS_SELECTOR,"textarea[id='currentAddress']")
   PERMANENT_ADDRESS=(By.CSS_SELECTOR,"textarea[id='permanentAddress']")
   SUBMIT=(By.CSS_SELECTOR,"button[id='submit']")

   #created form
   CREATED_FULL_NAME =(By.CSS_SELECTOR,"#output #name")
   CREATED_EMAIL = (By.CSS_SELECTOR,"#output #email")
   CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,"#output #currentAddress")
   CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR,"#output #permanentAddress")

class CheckBoxPageLocators:
   EXPAND_ALL_BUTTON=(By.CSS_SELECTOR,"button[title='Expand all']")
   ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
   CHEKED_ITEMS=(By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
   TITLE_ITEM=".//ancestor::span[@class='rct-text']"
   OUTPUT_RESULT=(By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators():
   YES_RADIOBUTTON=(By.CSS_SELECTOR,".custom-control-label[for='yesRadio']")
   IMPRESSIVE_RADIOBUTTON=(By.CSS_SELECTOR,".custom-control-label[for='impressiveRadio']")
   NO_RADIOBUTTON=(By.CSS_SELECTOR,".custom-control-label[for='noRadio']")
   OUTPUT_RESULT=(By.CSS_SELECTOR, ".text-success")

class WebPageLocators():
   #add person form
   ADD_USER_BUTTON=(By.CSS_SELECTOR,"button[id='addNewRecordButton']")
   FIRST_NAME_INPUT=(By.CSS_SELECTOR,"input[id='firstName']")
   LAST_NAME_INPUT=(By.CSS_SELECTOR,"input[id='lastName']")
   EMAIL_INPUT=(By.CSS_SELECTOR,"input[id='userEmail']")
   AGE_INPUT=(By.CSS_SELECTOR,"input[id='age']")
   SALARY_INPUT=(By.CSS_SELECTOR,"input[id='salary']")
   DEPARTMENT_INPUT=(By.CSS_SELECTOR,"input[id='department']")
   SUBMIT_BUTTON=(By.CSS_SELECTOR,"button[id='submit']")

   #tables
   FULL_PEOPLE_LIST=(By.CSS_SELECTOR,"div[class='rt-tr-group']")
   SEARCH_INPUT=(By.CSS_SELECTOR,"input[id='searchBox']")
   DELETE_BUTTON=(By.CSS_SELECTOR,"span[title='Delete']")
   ROW_PARENT=".//ancestor::div[@class='rt-tr-group']"

