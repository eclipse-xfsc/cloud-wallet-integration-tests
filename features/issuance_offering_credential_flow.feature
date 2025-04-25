Feature: Testing the credential issuance and offering flow

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in and on Issuance page
    Given Web UI cPCM is up
    And User is logged in
    And User is on Issuance page

  Scenario: User issues a credential then creates an offering with DID
    When we create an issuance with UUID and 'testName'
    Then fill offering with link from issuance
    Then the credential added on overview with UUID


