from behave import *

@Given('The user is logged into the application')
def step_impl(context):
    context.login_page.navigate_to_homepage()


@When('User clicks on the Search field')
def step_impl(context):
    context.home_page.click_search_grid()


@When('User inserts a valid item "vlad"')
def step_impl(context):
    context.home_page.insert_element()


@When('User clicks on the search button')
def step_impl(context):
    context.home_page.click_search_button()


@Then('the corresponding item "vlad" is returned')
def step_impl(context, valid_item):
    context.home_page.check_valid_item(valid_item)

@When('User inserts special characters "!@#$%^&*" into search field')
def step_impl(context, special_characters):
    context.home_page.insert_special_characters()
