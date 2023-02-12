import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if the user can log in by providing correct credentials.
    def test_login_successful(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        self.get_element_with_name("email").send_keys("jacek.s+mateuszm@zaplify.com")
        self.get_element_with_name("password").send_keys("interview")
        self.get_element_with_text("span", "Log in").click()
        self.wait_for_element_with_text_to_be_displayed("span", "Create Campaign")
        logged_in_successfully = self.get_element_with_text("span", "Create Campaign")
        assert logged_in_successfully

