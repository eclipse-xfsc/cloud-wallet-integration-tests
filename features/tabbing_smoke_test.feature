Feature: Smoke test for selecting tabs randomly and check for errors

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in
    Given Web UI cPCM is up
      And User is logged in
      And sidebar is visible

  Scenario: User chaos clicking on sidebar
    When we have options selected randomly
    Then the click selected options and check if loaded correctly
