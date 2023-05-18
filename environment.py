from pages.add_user_page import Add_user_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()
    context.add_user_page = Add_user_page()
    context.browser.maximise_window()


def after_all(context):
    context.browser.close_browser()