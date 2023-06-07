from behave import *

@When('The user clicks on the Add module')
def step_impl(context):
    context.home_page.click_add_module


@When('The user inserts value "vlad" in the First Name field')
def step_impl(context):
    context.add_person.insert_element
@When('The user clicks Save button')
def step_impl(context):
    context.add_person.click_save_button

@Then('The Person is successfully created')
def step_impl(context):
    context.add_person_check_url()