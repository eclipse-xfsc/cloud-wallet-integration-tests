Feature: Access Control Testing
  As a user, I should not be able to access restricted pages without logging in.

  Background: cPCM is up and running
    Given Web UI cPCM is up

  Scenario: Access restricted page without login
    Given I am not logged in
    When User tries to access a restricted page
    Then User should be redirected to the login page