from behave import *



@When('The user clicks on the People module')
def step_impl(context):
    context.home_page.click_people_module()

@Then('The user is on the People module')
def step_impl(context):
    context.people_module.check_url()

@Then('The Delete button is displayed')
def step_impl(context):
    context.people_module.is_displayed()