import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    #webdriver.Chrome(
       ## service=Service(r"C:/Users/Arren/Documents/GitHub/ProgKymalov" + "chromedriver.exe")
       # )
    
    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, "login_field")

    login_elem.send_keys("arren667@gmail.com")
    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrong_password")
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()
    assert driver.title == "Sign in to GitHub · GitHub"
    #time.sleep(3)

    driver.close