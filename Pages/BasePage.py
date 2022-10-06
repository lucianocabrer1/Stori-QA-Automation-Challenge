from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        el.click()

    def send_key(self, locator, text):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        el.send_keys(text)
    
    def find_element_xpath(self, locator):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return el
    
    def find_elements_xpath(self, locator):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return el
    
    def find_element_class(self, locator):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return el

    def highlight(self, element, effect_time, color, border):
        """Highlights (blinks) a Selenium Webdriver element"""
        self.driver = element._parent
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                element, s)
        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)
    
    def alert(self):
        alerts = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alerts.accept()