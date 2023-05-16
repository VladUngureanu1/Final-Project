from pages.base_page import BasePage


class LoginPage(BasePage):

    def navigate_to_homepage(self):
        self.chrome.get("https://jules.app/sign-in")
