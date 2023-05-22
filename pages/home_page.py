

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage


class HomePage(BasePage):
    ACCOUNT_DROPDOWN = (By.XPATH, '//*[@data-test-id="user-options-business-button"]')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Type and Search..."]')
    SEARCH_BUTTON = (By.XPATH, '//*[@class="MuiSvgIcon-root jss18"]')
    VALID_ITEM = (By.XPATH, '//div//span[text()="vlad"]')



    def logout_of_the_application(self):
        self.chrome.find_element(*self.ACCOUNT_DROPDOWN).click()
        self.chrome.find_element(*self.LOGOUT_LINK).click()

    def click_search_grid(self):
        self.chrome.find_element(*self.SEARCH_FIELD).click()

    def insert_element(self, insert_element='vlad'):
        element=(self.SEARCH_FIELD)
        element.send_keys(insert_element)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_valid_item(self):
        self.chrome.find_element(*self.VALID_ITEM)
    assert

    def insert_special_characters(self, inserts_special_characters='!@#$%^&*'):
        specials_characters=(self.SEARCH_FIELD)
        specials_characters.send_keys(inserts_special_characters)
    assert

