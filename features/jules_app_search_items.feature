Feature: Check if we can search items into application

  Background:
    Given The user is logged into the application
    When User clicks on the Search field
    When User clicks on the search button

  @T1
  Scenario:
    When User inserts a valid item 'vlad'
    Then The corresponding item 'vlad' is returned


  @T2
  Scenario:
    When User inserts special characters '!@#$%^&*' into search field
    Then No item is  returned
