Feature: Check if we can add a person


  Scenario:
    Given The user is logged into the application
    When The user clicks on the Add module
    When The user clicks on the Person field
    When The user inserts a value in the First Name field
    When The user clicks Save button
    Then The Person is successfully created
