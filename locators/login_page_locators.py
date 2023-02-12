from selenium.webdriver.common.by import By

class LoginPageLocators:
    email = By.NAME, "email"
    login_button_active = By.CLASS_NAME,"MuiButtonBase-root MuiButton-root MuiButton-contained button active MuiButton-disableElevation"
    login_button_inactive = By.CLASS_NAME, "MuiButtonBase-root MuiButton-root MuiButton-contained button disabled MuiButton-disableElevation"
    reveal_password = By.XPATH, "//input[@name='password']//parent::div//following-sibling::div//button//span//*[name()='svg']//*"
    revealed_password = By.XPATH, "//input[@value='ThisPasswordIsNotCorrect']"
    required_error = By.XPATH, "//p[text()='Required']"
    empty_password_error = By.XPATH, "//p[text()='You must type in a password']"
    invalid_email_address = By.XPATH, "//p[text()='Invalid email address']"
    login_page_header = By.XPATH, "//p[text()='Welcome back']"
    login_page_welcome_message = By.XPATH, "//p[text()='Let’s have an efficient day. Log in to keep up with new opportunties.']"
