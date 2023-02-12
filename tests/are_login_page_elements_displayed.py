import time

from selenium.webdriver import Keys

from page_object.login_page import LoginPage
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):
    #This test case verifies if the following elements are displayed on the login page:
    #1. The header containing the text 'Welcome back'
    #2. The paragraph containing the text 'Let’s have an efficient day. Log in to keep up with new opportunties.'
    def test_login_successful(self):
        page = LoginPage(self.driver)
        self.wait_for_element_with_text_to_be_displayed("p", "Welcome back")
        is_login_page_header_displayed = page.is_login_page_header_displayed
        is_login_page_welcome_message_displayed = page.is_login_page_welcome_message
        assert is_login_page_header_displayed
        assert is_login_page_welcome_message_displayed