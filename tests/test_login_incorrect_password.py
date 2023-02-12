import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies in an incorrect password error message is displayed whenever the user provides an incorrect
    #password
    def test_login_unsuccessfull_incorrect_password(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("jacek.s+mateuszm@zaplify.com")
        self.get_element_with_name("password").send_keys("ThisPasswordIsNotCorrect")
        self.get_element_with_text("span", "Log in").click()
        self.wait_for_element_with_text_to_be_displayed("span","Email or password incorrect")
        login_error_message = self.get_element_with_text("span","Email or password incorrect")
        assert login_error_message