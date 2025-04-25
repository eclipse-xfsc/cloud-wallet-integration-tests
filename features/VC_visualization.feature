Feature: Ability to see VC added and select them to see details

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in
    Given Web UI cPCM is up
    And User is logged in

  Scenario: User have credentials present and can open them
    Given credential cards are on screen
    When the user clicks on a VC
    Then the selected VC details appear