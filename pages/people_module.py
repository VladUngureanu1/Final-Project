from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class PeopleModule(HomePage):


    DELETE_BUTTON = (By.ID, 'batch-delete-button')



    def check_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://jules.app/people'
        assert expected_url == actual_url, f'The Url is incorrect, check People module'

    def is_displayed(self):
        self.chrome.find_element(*self.DELETE_BUTTON).is_displayed()
        assert self.chrome.find_element(*self.DELETE_BUTTON).is_displayed()