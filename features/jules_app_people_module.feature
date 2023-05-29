Feature: Check that the People module of the Jules_app is working properly

    Background:
      Given The user is logged into the application
      When The user clicks on the People module


    @T1
    Scenario:
      Then The user is on the People module

    @T2
    Scenario:
      Then The Delete button is displayed


