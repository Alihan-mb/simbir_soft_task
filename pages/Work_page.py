import time

from selenium.webdriver.common.by import By

from pages.All_methods import AllMethods


class Deposit_Withdraw(AllMethods):
    """Locators"""
    """Login Page"""
    customer_login = (By.XPATH, "//*[text()='Customer Login']")
    dropdown = (By.XPATH, "//select")
    login_button = (By.XPATH, "//button[@type='submit']")
    account_name = (By.CSS_SELECTOR, ".fontBig")

    """Depositing"""
    deposit_button = (By.XPATH, "//button[@ng-class='btnClass2']")
    amount_field = (By.XPATH, "//input[@placeholder]")
    submit_button = (By.XPATH, "//button[@type='submit']")
    success_message = (By.CSS_SELECTOR, ".error")
    withdrawal_success = (By.XPATH, "//*[text()='Transaction successful']")
    balance = (By.CSS_SELECTOR, ".center strong:nth-child(2)")
    withdraw_button = (By.XPATH, "//button[@ng-click='withdrawl()']")

    """Transactions"""
    transaction_page = (By.XPATH, "//button[@ng-click='transactions()']")
    transaction_count = (By.XPATH, "//tbody//tr")

    def __init__(self, driver):
        super().__init__(driver)

    def logging_in(self, value):
        self.clicking_element(locator=self.customer_login)
        dropdown = self.returning_web_element(self.dropdown)
        select = self.select_dropdown(dropdown)
        select.select_by_visible_text(value)
        self.clicking_element(self.login_button)

    def checking_login_success(self):
        return self.returning_web_element(self.account_name)

    def depositing(self, fib_number):
        self.clicking_element(self.deposit_button)
        self.sending_keys(locator=self.amount_field, text=fib_number)
        self.clicking_element(self.submit_button)
        return self.returning_web_element(self.success_message)

    def checking_balance(self):
        return self.returning_web_element(self.balance)

    def withdrawing(self, fib_number):
        self.clicking_element(self.withdraw_button)
        time.sleep(1)
        self.sending_keys(locator=self.amount_field, text=fib_number)
        self.clicking_element(self.submit_button)
        return self.returning_web_element(self.withdrawal_success)

    def transactions(self):
        self.clicking_element(self.transaction_page)
        return self.returning_web_elements(self.transaction_count)

    def csv(self):
        return self.returning_web_elements(self.transaction_count)




















