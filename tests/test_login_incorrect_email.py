import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if a login error message is being displayed whenever the user provides a wrong email address
    def test_login_unsuccessfull_incorrect_password(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("jacek.s+mateuERRORszm@zaplify.com")
        self.get_element_with_name("password").send_keys("interview")
        self.get_element_with_text("span", "Log in").click()
        self.wait_for_element_with_text_to_be_displayed("span","The password or email you entered is incorrect.")
        login_error_message = self.get_element_with_text("span","The password or email you entered is incorrect.")
        assert login_error_message