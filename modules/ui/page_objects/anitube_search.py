#індивідуальна робота

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AnimeSearch(BasePage):
    URL:'https://anitube.in.ua/'

    def __init__(self) -> None:
        super().__init__()  
    def go_to(self):
        self.driver.get(AnimeSearch.URL)
    
    def try_search(self):
        search_element = self.driver.find_element(By.ID, "story")
        search_element.send_keys()

        btn_start_srch = self.driver.find_element(By.CLASS_NAME, "search_btn_on")
        btn_start_srch.click()

        field_name = self.driver.find_element(By.NAME, "name")
        field_name.send_keys("Velentyn")

        field_email = self.driver.find_element(By.NAME, "email")
        field_email.send_keys("arren777@gmail.com")

        field_subject = self.driver.find_element(By.NAME, "subject")
        field_subject.send_keys("Top 10 anime")

        field_message = self.driver.find_element(By.NAME, "message")
        field_message.send_keys("Thanks for your work!")

        #кнопка відправки закоментована нижче
        #sent_feedback = self.driver.find_element(By.XPATH, '//a[@href="/index.php?do=feedback" and @title="Зворотній зв\'язок"]')
        #sent_feedback.click()
        
    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
    def feedback_amtb(self):
        feedback_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/index.php?do=feedback"][title="Зворотній зв\'язок"]')

        feedback_btn.click()

        