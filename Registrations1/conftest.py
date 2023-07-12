import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    driver.get("https://www.facebook.com/signup")
    #driver.find_element(By.ID, "reg_click_here").click()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
