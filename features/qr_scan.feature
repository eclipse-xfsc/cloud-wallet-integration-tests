Feature: Ability to scan a QR code to accept connection

  Scenario: Generating a QR code
    Given QR generating service working
    Given navigate to QR generating page
    When we created a QR code
      And saved it to our folder
    Then we navigate to QR url
      And we are at the desired page
