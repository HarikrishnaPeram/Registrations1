from selenium.webdriver.support.select import Select



from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class Testendtoend(BaseClass):
    def test_etoe(self):
     #Basic info page
        basicinfo = BasicInfo(self.driver)