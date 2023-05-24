from behave import *

@Given('The user is logged into the application')
def step_impl(context):
    context.login_page.navigate_to_homepage()


@When('User clicks on the search field')
def step_impl(context):
    context.home_page.click_search_field()


@When('User inserts a valid item "vlad"')
def step_impl(context):
    context.home_page.insert_element()


@When('User clicks on the search button')
def step_impl(context):
    context.home_page.click_search_button()


@Then('the corresponding "{search_item}" is returned')
def step_impl(context, search_item):
    context.home_page.check_valid_item(search_item)

@When('User inserts special characters "{special_characters}" into the search field')
def step_impl(context, special_characters):
    context.home_page.insert_special_characters(special_characters)
