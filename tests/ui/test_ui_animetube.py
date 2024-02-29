#індивідуальна робота

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""В цьому тесті реалізоване відкриття сайту https://anitube.in.ua/
вписування певного тайтлу в рядок пошуку і натискання клавіши пошуку.
В кінці тесту також реалізована перевірка переходу на очікувану
сторінку та закриття браузера"""

@pytest.mark.ui
def test_anime_search():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    driver.get("https://anitube.in.ua/")

    search_element = driver.find_element(By.ID, "story")
    search_element.send_keys("One piece")
    btn_start_srch = driver.find_element(By.CLASS_NAME, "search_btn_on")
    btn_start_srch.submit()

    assert driver.title == "Пошук на сайті » AniTube - аніме онлайн українською"
     
    
    driver.close

"""Цей код тестує відкриття сайту https://anitube.in.ua/, перехід
до кнопки "Зворотній зв'язок" та заповнення відповідних полів.
Кнопка відправки повідомлення також реалізована, але закоментована"""

@pytest.mark.ui
def test_feedback_amtb():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    driver.get("https://anitube.in.ua/")

    feedback_btn = driver.find_element(By.CSS_SELECTOR, 'a[href="/index.php?do=feedback"][title="Зворотній зв\'язок"]')
    feedback_btn.click()

    assert driver.title == "Зворотний зв’язок » AniTube - аніме онлайн українською"

    field_name = driver.find_element(By.NAME, "name")
    field_name.send_keys("Velentyn")

    field_email = driver.find_element(By.NAME, "email")
    field_email.send_keys("arren777@gmail.com")

    field_subject = driver.find_element(By.NAME, "subject")
    field_subject.send_keys("Top 10 anime")

    field_message = driver.find_element(By.NAME, "message")
    field_message.send_keys("Thanks for your work!")

    #кнопка відправки закоментована нижче
    #sent_feedback = driver.find_element(By.XPATH, '//a[@href="/index.php?do=feedback" and @title="Зворотній зв\'язок"]')
    #sent_feedback.click()   
    
    driver.close()
    



