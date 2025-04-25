Feature: As a user, I want to be able to log in and access the account page and log out

  Scenario: Log in Web UI cPCM
    Given Web UI cPCM is up
    Given the user is on cPCM Login page
      And input valid credentials provided
    When login to cPCM
    Then the next page is Account page

  Scenario: Log out
    Given Web UI cPCM is up
    Given the user successfully logged in to cPCM
    When log out option is visible
    Then I logout
      And I am logged out
