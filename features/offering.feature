Feature: Testing the offering page with static data

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in and on Offering page
    Given Web UI cPCM is up
    And User is logged in
    And User is on Offering page

  Scenario: User clicks on Add button and paste a static link to offering
    When we click on Add button
    Then fill offering link with static url
    When click offering submit
    Then an offering appears on screen and accept
    And clicked on accept and a DID selected

