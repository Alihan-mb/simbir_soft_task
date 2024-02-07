from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class AllMethods:

    def __init__(self, driver):
        self.driver = driver

    def clicking_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def returning_web_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def returning_web_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def select_dropdown(self, web_ele):
        select = Select(web_ele)
        return select

    def sending_keys(self, locator, text):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        ele.send_keys(text)
