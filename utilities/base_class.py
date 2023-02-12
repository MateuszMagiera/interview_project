import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setUp")
class BaseClass:
    def wait_for_element_with_text_to_be_displayed(self,element,text):
        return WebDriverWait(self.driver,15).until(expected_conditions.presence_of_element_located((By.XPATH,"//"+element+"[text()='"+text+"']")))

    def get_element_with_text(self, element, text):
        return self.driver.find_element(By.XPATH,"//"+element+"[text()='"+text+"']")

    def get_element_with_name(self,name):
        return self.driver.find_element(By.NAME,""+name+"")