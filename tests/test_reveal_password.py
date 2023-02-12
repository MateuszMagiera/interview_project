import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if the password is being revealed after clicking on a proper icon.
    def test_login_unsuccessfull_incorrect_password(self):
        page = LoginPage(self.driver)
        wait = WebDriverWait(self.driver,5)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("jacek.s+mateuszm@zaplify.com")
        self.get_element_with_name("password").send_keys("ThisPasswordIsNotCorrect")
        reveal_password = page.reveal_password
        reveal_password.click()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@value='ThisPasswordIsNotCorrect']")))
        password_has_been_revealed = page.revealed_password
        time.sleep(3)
        assert password_has_been_revealed