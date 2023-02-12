import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if an error message appears beneath the password input whenever the user provides an
    #empty password
    def test_login_successful(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("jacek.s+mateuszm@zaplify.com")
        self.get_element_with_name("password").send_keys("")
        self.get_element_with_name("email").click()
        self.wait_for_element_with_text_to_be_displayed("p","You must type in a password")
        is_empty_password_error_message_displayed = page.empty_password_error_message
        assert is_empty_password_error_message_displayed