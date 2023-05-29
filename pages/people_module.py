from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PeopleModule(BasePage):

    PEOPLE_MODULE = (By.ID, 'people-navigation-button')
    DELETE_BUTTON = (By.ID, 'batch-delete-button')

    def click_people_module(self):
        self.chrome.find_element(self.PEOPLE_MODULE).click()

    def check_url(self):
        actual_url = 'https://jules.app/search/all'
        expected_url = 'https://jules.app/people'
        assert expected_url == actual_url, f'The Url is incorrect, check People module'

    def is_displayed(self):
        self.chrome.find_element(self.DELETE_BUTTON).is_displayed()
        assert self.chrome.find_element(self.DELETE_BUTTON).is_displayed()