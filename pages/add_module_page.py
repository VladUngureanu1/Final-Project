from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AddModule(BasePage):


    PERSON_FIELD = (By.XPATH, '//div[@data-test-id="person-wizard-tile"]')
    # FIRST_NAME = (By.)


    def click_person_field(self):
        self.chrome.find_element(*self.PERSON_FIELD).click()