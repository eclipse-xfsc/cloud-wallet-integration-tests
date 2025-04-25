Feature: : Able to change the user preferences on language, event logs and save settings

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in and on the wallet backup screen
    Given Web UI cPCM is up
    And User is logged in
    And User is on Settings screen


  Scenario: User can change the cPCM language
    Given language options is presented
    When the user changes language
    Then the cPCM is displayed in a different language

  Scenario: User can change the length of the history log
    Given history log option is presented
    When the user selects a different length
    And navigates to the event log
    Then the amount of events displayed matches the log length
