from behave import *


@given("The user is on the Jules_app homepage")
def step_impl(context):
    context.login_page.navigate_to_homepage()
