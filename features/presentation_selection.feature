Feature: Testing the credential issuance and offering flow

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    # VP = verifiable presentation


  Background: User is logged in and on Issuance page
    Given Web UI cPCM is up
    And User is logged in
    And User is on Presentation Selection page

  Scenario: User creates verifiable presentation
    When user selects IDs for Presentation
      And selects the DID for Presentation
    Then the presentation can be viewed by verifier
