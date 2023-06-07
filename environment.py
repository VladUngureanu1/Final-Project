from pages.add_person_page import AddPerson
from pages.home_page import HomePage
from pages.login_page import LoginPage
from browser import Browser
from pages.people_module import PeopleModule


class AddModule:
    pass


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()
    context.add_module = AddModule()
    context.add_person = AddPerson()
    context.people_module = PeopleModule()
    context.browser.maximise_window()


def after_all(context):
    context.browser.close_browser()