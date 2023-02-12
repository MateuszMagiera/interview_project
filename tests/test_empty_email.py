import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if the error appears beneath the email input whenever the user provides an empty email
    def test_login_successful(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("")
        self.get_element_with_name("password").send_keys("interview")
        self.wait_for_element_with_text_to_be_displayed("p","Required")
        is_required_error_message_displayed = page.required_error_message
        assert is_required_error_message_displayed