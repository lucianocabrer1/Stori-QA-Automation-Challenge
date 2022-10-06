import pytest
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest

class Test_HomePage(BaseTest):
    
    def test_select_country_Mexico(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.search_country("Me", "Mexico")
        assert rta == 1
    
    def test_select_option(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.search_dropdown("Option2")
        rta2 = self.homepage.search_dropdown("Option3")
        assert rta == rta2 == 1
    
    def test_side_tab(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.change_tab()
        assert rta == 1

    def test_switch_window(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.change_page_and_check_string()
        assert rta == 1
    
    def test_check_table(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.check_price_table()
        assert rta != 0

    def test_check_table_Engineer(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.check_engineer_table()
        assert rta != 0

    def test_highlight_text(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.highlightText()
        assert rta == 1

    def test_alertbox(self):
        self.homepage = HomePage(self.driver)
        rta = self.homepage.alertbox("Stori card")
        assert rta == 1
    