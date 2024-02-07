import time

import allure
from allure import severity, severity_level
import pytest
from datetime import datetime
from utilities.base_class import BaseClass
from configurations.config import Test_Data
from utilities.fibonaci import result
from pages.Work_page import Deposit_Withdraw

base_path = "C:/Users/a.magomedaliev/PycharmProjects/pythonProject/selenium_grid"


class Test_XYZ(BaseClass):

    @allure.severity(severity_level=severity_level.BLOCKER)
    def test_login(self):
        allure.step("Step 1: Logging in")
        login_page = Deposit_Withdraw(self.driver)
        login_page.logging_in(Test_Data.ACCOUNT_NAME)
        account_name = login_page.checking_login_success()
        assert account_name.text == Test_Data.ACCOUNT_NAME, allure.attach(body=f"Login failed, account name is {account_name.text}",
                                                                          name="Login Status",
                                                                          attachment_type=allure.attachment_type.TEXT)

    @allure.severity(severity_level=severity_level.CRITICAL)
    def test_deposit(self):
        allure.step("Step 2: Making a deposit")
        deposit_withdraw = Deposit_Withdraw(self.driver)
        deposit_success_msg = deposit_withdraw.depositing(result)
        balance = deposit_withdraw.checking_balance()
        assert deposit_success_msg.text == Test_Data.DEPOSIT_SUCCESS
        assert int(balance.text) == result, allure.attach(
            body=f"balance is not equal to the fibonnachi number, balance is"
            f"{balance.text}", name="Deposit Status",
            attachment_type=allure.attachment_type.TEXT)

    @allure.severity(severity_level=severity_level.CRITICAL)
    def test_withdrawing(self):
        allure.step("Step 3: Withdrawing the deposited amount")
        log = self.getLogger()
        deposit_withdraw = Deposit_Withdraw(self.driver)
        withdraw_success_msg = deposit_withdraw.withdrawing(result)
        balance = deposit_withdraw.checking_balance()
        log.info(withdraw_success_msg.text)
        assert withdraw_success_msg.text == Test_Data.WITHDRAWAL_SUCCESS
        assert int(balance.text) == 0, allure.attach(f"Withdrawal was not successful, balance is {balance.text}",
                                                     name="Withdrawal status",
                                                     attachment_type=allure.attachment_type.TEXT)

    @allure.severity(severity_level=severity_level.CRITICAL)
    def test_transactions(self):
        allure.step("Step 4: Checking if transactions are present on the transaction page")
        log = self.getLogger()
        deposit_withdraw = Deposit_Withdraw(self.driver)
        time.sleep(1)
        transactions = deposit_withdraw.transactions()
        log.info(f"there are {len(transactions)} transactions")
        assert len(transactions) == 2, allure.attach(f"transaction count is not 2, it's {len(transactions)}",
                                                     name="Transaction count",
                                                     attachment_type=allure.attachment_type.TEXT)

    @allure.severity(severity_level=severity_level.NORMAL)
    def test_csv(self):
        allure.step("Step 5: Creating a csv file")
        log = self.getLogger()
        deposit_withdraw = Deposit_Withdraw(self.driver)
        tr_list = [item.text for item in (deposit_withdraw.csv())]
        assert len(tr_list) > 0
        for transaction_data in tr_list:
            date_list = transaction_data.splitlines()
            stripped_list = date_list[0].strip(",").split(" ")
            log.info(stripped_list)
            allure.description("Here are we formatting info to be passed to csv")
            transaction_time = stripped_list[3] + '' + stripped_list[4]
            formatted_csv = ("{day} {month}_{year}_{hour_min_sec}, amount is={amount}, transaction type is={tr_type}".
                             format(day=stripped_list[1],
                                    month=stripped_list[0],
                                    year=stripped_list[2],
                                    hour_min_sec=transaction_time,
                                    amount=stripped_list[5],
                                    tr_type=stripped_list[6]))

            with open(file=f"{base_path}/reports/simbir.csv",
                      mode="a") as file:
                file.write(f"{formatted_csv}\n")

            allure.attach(body=f"{base_path}/reports/simbir.csv", name="CSV_FILE",attachment_type=allure.attachment_type.CSV)
            with open(file=f"{base_path}/reports/simbir.csv", mode="r") as simbir:
                csv_data = simbir.read()
                assert "amount is" and "transaction type is" in csv_data
                assert str(result) in csv_data, allure.attach(body="Fibonnachi number is not in the csv", name="Csv contents",
                                                              attachment_type=allure.attachment_type.TEXT)
