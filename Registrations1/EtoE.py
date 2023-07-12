from selenium.webdriver.support.select import Select


from Registrations1.Basicinfo import BasicInfo
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class Testendtoend(BaseClass):
    def test_etoe(self):
     #Basic info page
        basicinfo = BasicInfo(self.driver)
         
        basicinfo.getfirstname().send_keys("Harikrishna")
        basicinfo.getconfirmfirstname().send_keys("Harikrishna")
        basicinfo.getmobileNo().send_keys("9876543211")
        basicinfo.getconfirmmobileNo().send_keys("9876543211")
        basicinfo.getemail().send_keys("Hari")
        sel = Select(basicinfo.getdropdown())
        sel.select_by_value("gmail.com")
        basicinfo.getconfirmemail().send_keys("Hari@gmail.com")
        basicinfo.getsaveandnext().click()

        photosign = PhotoSignature(self.driver)

        photosign.getphoto().send_keys("D:\Hari\Images\Krishna.jpg")
        photosign.getsignature().send_keys("D:\Hari\Images\kumar_sign.jpg")
        photosign.getCheckBoxPhoto().click()
        photosign.getCheckBoxSignature().click()
        photosign.getnext().click()

     
         













