import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Type and Search..."]')
    SEARCH_BUTTON = (By.XPATH, '//*[@class="MuiSvgIcon-root jss18"]')
    VALID_ITEM = (By.XPATH, '//div//span[text()="vlad"]')
    PEOPLE_MODULE = (By.XPATH, '//div[@data-test-id="people-navigation-button"]')
    ADD_MODULE = (By.XPATH, '//div[@data-test-id="add-flows-navigation-button"]')



    def click_search_field(self):
        time.sleep(10)
        self.chrome.find_element(*self.SEARCH_FIELD).click()

    def insert_element(self, insert_element='vlad'):
        element = self.chrome.find_element(*self.SEARCH_BUTTON)
        element.send_keys(insert_element)

    def click_search_button(self):
        time.sleep(10)
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_current_item(self, search_item):
        current_item = self.chrome.find_element(*self.VALID_ITEM).text
        assert current_item == search_item, f' The returned item is not the same'

    def insert_special_characters(self, special_characters):
        search_field = self.chrome.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(special_characters)

    def click_people_module(self):
        time.sleep(10)
        self.chrome.find_element(*self.PEOPLE_MODULE).click()

    def click_add_module(self):
        self.chrome.find_element(*self.ADD_MODULE).click()







