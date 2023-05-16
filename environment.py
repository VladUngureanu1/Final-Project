from pages.loginpage import LoginPage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()

def after_all(context):
    context.browser.close_browser()