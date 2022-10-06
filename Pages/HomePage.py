
from Pages.BasePage import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import logging
from datetime import datetime

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class HomePage(BasePage):

    COUNTRY = (By.XPATH, "//*[@id=\"autocomplete\"]")
    DROPDOWN = (By.XPATH, "//select[@id=\"dropdown-class-example\"]")
    COUNTRY_LIST = (By.XPATH, "//li[@class='ui-menu-item']")
    WINDOW = (By.ID, "openwindow")
    TEXT = (By.XPATH, "//*[contains(text(),\"30 day Money Back Guarantee\")]")
    VIEWALL = (By.XPATH, "//*[contains(text(),\"VIEW ALL COURSES\")]")
    SIDE = (By.XPATH, "//*[@id=\"opentab\"]")
    TABLE = (By.XPATH, "//*[@name=\"courses\"]/tbody/tr")
    TABLEFIX = (By.XPATH, "//*[contains(@class, \"tableFixHead\")]/table/tbody/tr")
    IFRAME = (By.XPATH, "//*[@id=\"courses-iframe\"]")
    TEXT_IFRAME = (By.XPATH, "/html/body/div/div[2]/section[4]/div/div/div/div[2]/ul/li[2]")
    ALERT_TEXT = (By.XPATH, "//*[@id=\"name\"]")
    ALERT_BTN_ALERT = (By.XPATH, "//*[@id=\"alertbtn\"]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    
    def search_country(self, country_text, fullCountry):
        self.click(self.COUNTRY)
        
        self.send_key(self.COUNTRY, country_text)
        
        time.sleep(2)

        suggestions = self.find_elements_xpath(self.COUNTRY_LIST)

        for element in suggestions:
            
            text = element.text
            
            if 'Mexico' in text:
                element.click()
                time.sleep(2)
                return 1
    
    def search_dropdown(self, option):

        self.click(self.DROPDOWN)
        
        element = self.find_element_xpath(self.DROPDOWN)

        sel = Select(element)

        sel.select_by_visible_text(option)

        time.sleep(2)

        return 1
    
    def change_tab(self):
        
        original_window = self.driver.current_window_handle

        assert len(self.driver.window_handles) == 1

        self.click(self.SIDE)

        child = self.driver.window_handles

        for tab in child:
            if tab != original_window:
                self.driver.switch_to.window(tab)

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        time.sleep(5)

        self.find_element_xpath(self.VIEWALL)

        dateTimeObj = datetime.now()

        timestampStr = dateTimeObj.strftime("%d-%b-%Y %H-%M-%S")

        self.driver.save_screenshot('./resources/change_tab' + str(timestampStr) + '.png')

        self.driver.close()

        self.driver.switch_to.window(original_window)

        return 1 

    def change_page_and_check_string(self):

        original_window = self.driver.current_window_handle

        assert len(self.driver.window_handles) == 1

        self.click(self.WINDOW)

        child = self.driver.window_handles

        for tab in child:
            if tab != original_window:
                self.driver.switch_to.window(tab)
        time.sleep(5)

        if self.find_element_xpath(self.TEXT):
            self.driver.close()
            self.driver.switch_to.window(original_window)
            return 1

    def check_price_table(self):
                
        el = self.find_elements_xpath(self.TABLE)

        i = 0 

        for a in range(len(el)):

            if(a >= 2):
                
                aux_td3 = "//*[@name=\"courses\"]/tbody/tr[" + str(a) + "]/td[3]"

                aux_td2 = "//*[@name=\"courses\"]/tbody/tr[" + str(a) + "]/td[2]"

                td3 = (By.XPATH, aux_td3)
                td2 = (By.XPATH, aux_td2)

                td3_25eq = self.find_element_xpath(td3)
                td2_25eq = self.find_element_xpath(td2)
                
                if '25' in td3_25eq.text:
                    print(td2_25eq.text)
                    self.highlight(td2_25eq, 3, "blue", 2)
                    i += 1

        return i

    def check_engineer_table(self):

        el = self.find_elements_xpath(self.TABLEFIX)

        i = 0 
 
        for a in range(len(el)):

            if(a >= 1):
                
                aux_td2 = "//*[contains(@class, \"tableFixHead\")]/table/tbody/tr[" + str(a) + "]/td[2]"

                aux_td1 = "//*[contains(@class, \"tableFixHead\")]/table/tbody/tr[" + str(a) + "]/td[1]"

                td2 = (By.XPATH, aux_td2)
                td1 = (By.XPATH, aux_td1)

                td2_Engineer_eq = self.find_element_xpath(td2)
                td1_Engineer_eq = self.find_element_xpath(td1)
                
                if 'Engineer' in td2_Engineer_eq.text:
                    print(td1_Engineer_eq.text)
                    self.highlight(td1_Engineer_eq, 3, "blue", 2)
                    i += 1

        return len(el)
    
    def highlightText(self):

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        self.driver.switch_to.frame(self.find_element_xpath(self.IFRAME))

        td1_Engineer_eq = self.find_element_xpath(self.TEXT_IFRAME)

        actions = ActionChains(self.driver)

        actions.move_to_element(td1_Engineer_eq).perform()

        self.highlight(td1_Engineer_eq, 3, "blue", 2)

        self.driver.switch_to.default_content()

        return 1
    
    def alertbox(self, cad):

        self.send_key(self.ALERT_TEXT, cad)

        self.click(self.ALERT_BTN_ALERT)

        self.alert()

        return 1
    