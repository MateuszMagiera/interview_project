import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if an error informing the user that wrong email format was used (no @ in the email input)
    def test_login_successful(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("test")
        self.get_element_with_name("password").send_keys("interview")
        self.wait_for_element_with_text_to_be_displayed("p", "Invalid email address")
        is_invalid_email_address_error_message_displayed = page.invalid_email_address_format
        assert is_invalid_email_address_error_message_displayed
