from selenium.webdriver.common.by import By


class PhotoSignature:

    def __init__(self, driver):
        self.driver = driver
    photo = (By.CSS_SELECTOR, "#picture")
    signature = (By.CSS_SELECTOR, "#signature")
    CheckBoxPhoto = (By.CSS_SELECTOR, "#confirmPhoto")
    CheckboxSignature= (By.CSS_SELECTOR, "#confirmSign")
    next =(By.CSS_SELECTOR, "#Submit")


    def getphoto(self):
        return self.driver.find_element(*PhotoSignature.photo)
    def getsignature(self):
        return self.driver.find_element(*PhotoSignature.signature)
    def getCheckBoxPhoto(self):
        return self.driver.find_element(*PhotoSignature.CheckBoxPhoto)

    def getCheckBoxSignature(self):
        return self.driver.find_element(*PhotoSignature.CheckboxSignature)
    def getnext(self):
        return self.driver.find_element(*PhotoSignature.next)

        photosign = PhotoSignature(self.driver)

        photosign.getphoto().send_keys("D:\Hari\Images\Krishna.jpg")
        photosign.getsignature().send_keys("D:\Hari\Images\kumar_sign.jpg")
        photosign.getCheckBoxPhoto().click()
        photosign.getCheckBoxSignature().click()
        photosign.getnext().click()

