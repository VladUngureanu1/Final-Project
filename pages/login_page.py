import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
class LoginPage(BasePage):

    USERNAME = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASSWORD = (By.XPATH, '//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//div[@id="client-snackbar"]//span')
    ACCOUNT_DROPDOWN = (By.XPATH, '//*[@data-test-id="user-options-business-button"]')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Type and Search..."]')

    def navigate_to_homepage(self):
        self.chrome.get("https://jules.app/sign-in")
    def insert_username(self, user_name = 'simebi2783@asuflex.com'):
        username = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.USERNAME))
        username.send_keys(user_name)

    def insert_password(self, user_password='Dacialogan2023!'):
        password = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located(self.PASSWORD))
        password.send_keys(user_password)
    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(5)

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://jules.app/search/all'
        assert expected_url == actual_url, f'The url is incorrect. Please check the login functionality'


    def check_login_error_message(self, expected_error_message):
        self.check_error_message(*self.LOGIN_ERROR_MESSAGE, expected_error_message)


