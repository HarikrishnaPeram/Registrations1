import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Registrations1.Basicinfo import select

driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)

#driver.get("https://regqc.sifyitest.com/kabodec22")
#driver.find_element(By.CSS_SELECTOR,".ca_regindex_container").click()
#driver.find_element(By.ID, "fullname").send_keys("Hari")
#driver.find_element(By.ID, "cfullname").send_keys("Hari")
#driver.find_element(By.ID, "txtmobile").send_keys(9876543211)
#driver.find_element(By.ID, "txtcmobile").send_keys(9876543211)
#driver.find_element(By.ID, "txtemail").send_keys("hari")
#dropdown = Select(driver.find_element(By.ID,"seldomain"))
#dropdown.select_by_index(2)
#driver.find_element(By.CSS_SELECTOR,"#txtcemail").send_keys("hari@gmail.com")
#driver.find_element(By.ID,"FinalSubmit").click()
#time.sleep(2)
#alert=driver.switch_to.alert
#alertText = alert.text
#print(alertText)
#alert.accept()

#driver.find_element(By.CSS_SELECTOR, "#picture").send_keys("D:\Hari\Images\Krishna.jpg")
#time.sleep(2)
#driver.find_element(By.CSS_SELECTOR,"#signature").send_keys("D:\Hari\Images\kumar_sign.jpg")
#driver.find_element(By.CSS_SELECTOR,"#confirmPhoto").click()
#driver.find_element(By.CSS_SELECTOR,"#confirmSign").click()
#driver.find_element(By.CSS_SELECTOR,"#Submit ").click()
driver.get("https://regqc.sifyitest.com/kabodec22//reg_details.php?q=ZDg3MzJhZGYzOTg3OTk0MmExZjIyZmY4YmYzMmFlODB8MjQ1MDAwMDMx")

#Basic details
driver.find_element(By.ID,"Recheck").click()


driver.find_element(By.XPATH,"(//input[@id='opt_cat'])[1]").click()
alert=driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()
driver.find_element(By.XPATH,"(//input[@id='optdisability'])[1]").click()
religion=Select(driver.find_element(By.CSS_SELECTOR,"#religion"))
religion.select_by_value("Hindu")
driver.find_element(By.XPATH, "(//input[@name='optminority'])[1]").click()
centre=Select(driver.find_element(By.CSS_SELECTOR,"#selexamcentre"))
centre.select_by_index(1)









