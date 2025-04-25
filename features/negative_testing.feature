Feature: Test negative cases (history limit, offering link)

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in and on the settings screen
    Given Web UI cPCM is up
    And User is logged in

  Scenario: Invalid negative number input
    Given User is on Settings screen
    And history log option is presented
    When the user selects an invalid value -5
    Then error message is presented

  Scenario: Valid boundary values
    Given User is on Settings screen
    And history log option is presented
    When the user selects a different length of 0
    And navigates to the event log
    Then the amount of events displayed matches the log length for empty and zero

    Given User is on Settings screen
    And history log option is presented
    When the user selects a different length of 999999999999999999
    And navigates to the event log
    Then the amount of events displayed matches the log length for max

  Scenario: Invalid offering link
    Given User is on Offering page
    When we click on Add button
    Then fill offering link with invalid url
    Then start listening for error on API lvl
    When click offering submit
    Then error message is presented on UI lvl