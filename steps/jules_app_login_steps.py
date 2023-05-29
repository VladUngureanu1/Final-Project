import time
from time import sleep

from behave import *
@given("The user is on the Jules_app login page")
def step_impl(context):
    context.login_page.navigate_to_homepage()

@When("The user inserts valid Email and valid Password")
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()

@When("The user clicks on the login button")
def step_impl(context):
    context.login_page.click_login_button()

@Then("The user is logged into the application")
def step_impl(context):
    context.login_page.check_current_url()
    time.sleep(5)

@When("The user logs out of the application")
def step_impl(context):
    context.login_page

@When('The user inserts  username "{email}" and  password "{password}"')
def step_impl(context, email, password):
    try:
        context.home_page.logout_of_the_application()
    except:
        pass
    context.login_page.insert_username(email)
    context.login_page.insert_password(password)

@Then('The user receives error message "{error_message}" and cannot login into the application')
def step_impl(context, error_message):
    context.login_page.check_error_message(error_message)