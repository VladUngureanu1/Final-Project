from behave import *


@When('The user clicks on the Person field')
def step_impl(context):
    context.add_module.click_person_field
