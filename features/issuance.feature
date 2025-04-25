Feature: Testing the Issuance flow - selecting schemas, UI check

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in and on Issuance page
    Given Web UI cPCM is up
    And User is logged in
    And User is on Issuance page

  Scenario: User clicks on a credential schema, fills data and able to copy the issued credential
    When we click on select for a schema
    Then fill schema details with UUID and 'testName'
    When click submit
    Then we can copy a link to offer a credential

