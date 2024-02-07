import time
from selenium.webdriver.common.by import By
from pages.All_methods import AllMethods
from pages.Work_page import Deposit_Withdraw

class Login_Page(AllMethods):

    """Locators"""
    customer_login = (By.XPATH, "//*[text()='Customer Login']")
    dropdown = (By.XPATH, "//select")
    login_button = (By.XPATH, "//button[@type='submit']")
    account_name = (By.CSS_SELECTOR, ".fontBig")

    def __init__(self, driver):
        super().__init__(driver)

    def logging_in(self, value):
        self.clicking_element(locator=self.customer_login)
        dropdown = self.returning_web_element(self.dropdown)
        select = self.select_dropdown(dropdown)
        select.select_by_visible_text(value)
        self.clicking_element(self.login_button)
        return Deposit_Withdraw(self.driver)
    def checking_login_success(self):
        return self.returning_web_element(self.account_name)
