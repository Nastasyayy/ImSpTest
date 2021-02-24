from .locators import MainPageLocators
from .base_page import BasePage
import time

class MainPage(BasePage):
    def spacebar_input(self):
        add_name = self.browser.find_element(*MainPageLocators.NAME).send_keys(" ")
        add_name = self.browser.find_element(*MainPageLocators.TEL).send_keys(" ")
        add_message = self.browser.find_element(*MainPageLocators.MES).send_keys(" ")
        add_email = self.browser.find_element(*MainPageLocators.EMAIL).send_keys("abc@abc.ru")
        add_button = self.browser.find_element(*MainPageLocators.BUTTON)
        add_button.click()
        try:
            self.browser.find_element(*MainPageLocators.ERR_MESSAGE)
        except Exception:
            assert 0, "No error message. Space bar input is valid"
        #time.sleep(1)
