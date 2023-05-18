import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage


class HomePage(BasePage):
    ACCOUNT_DROPDOWN = (By.XPATH, '//*[@data-test-id="user-options-business-button"]')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')

    time.sleep(5)
    def logout_of_the_application(self):
        account_dropdown = WebDriverWait(self.chrome,20).until(EC.presence_of_element_located(self.ACCOUNT_DROPDOWN))
        account_dropdown.click()
        self.chrome.find_element(*self.LOGOUT_LINK).click()