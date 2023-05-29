from pages.add_user_page import Add_user_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from browser import Browser
from pages.people_module import PeopleModule


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()
    context.add_user_page = Add_user_page()
    context.people_module = PeopleModule()
    context.browser.maximise_window()


def after_all(context):
    context.browser.close_browser()