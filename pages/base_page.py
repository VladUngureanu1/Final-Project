from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser
from selenium.webdriver.support import expected_conditions as EC

class BasePage(Browser):

    def check_error_message(self, by, selector, expected_error_message):
        error_message_web_element = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located((by, selector)))
        actual_error_message_text = error_message_web_element.text
        assert expected_error_message == actual_error_message_text, f"Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}"
