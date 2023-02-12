from locators.login_page_locators import LoginPageLocators
from utilities.base_class import BaseClass


class LoginPage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    @property
    def reveal_password(self):
        return self.driver.find_element(*LoginPageLocators.reveal_password)

    @property
    def revealed_password(self):
        return self.driver.find_element(*LoginPageLocators.revealed_password)

    @property
    def inactive_login_button(self):
        return self.driver.find_element(*LoginPageLocators.login_button_inactive)

    @property
    def active_login_button(self):
        return self.driver.find_element(*LoginPageLocators.login_button_active)

    @property
    def required_error_message(self):
        return self.driver.find_element(*LoginPageLocators.required_error)

    @property
    def empty_password_error_message(self):
        return self.driver.find_element(*LoginPageLocators.empty_password_error)

    @property
    def invalid_email_address_format(self):
        return self.driver.find_element(*LoginPageLocators.invalid_email_address)

    @property
    def is_login_page_header_displayed(self):
        return self.driver.find_element(*LoginPageLocators.login_page_header)

    @property
    def is_login_page_welcome_message(self):
        return self.driver.find_element(*LoginPageLocators.login_page_welcome_message)