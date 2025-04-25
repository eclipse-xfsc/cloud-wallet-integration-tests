Feature: User can create and download backups

    ## PCM = Personal credential manager
    ## cPCM = cloud personal credential manager
    ## VC = verifiable credential
    ## VP = verifiable presentation


  Background: User is logged in and on the wallet backup screen
    Given Web UI cPCM is up
    And User is logged in
    And User is on cPCM Wallet backup screen

    Scenario: User can perform backup sequence
      When user create a backup in the UI with name 'MarkBackup'
      Then scans the 'upload' link from screen
        And upload a file
      Then click the 'download' with the matching name
        And download the file
      Then compare files
        And files are matching