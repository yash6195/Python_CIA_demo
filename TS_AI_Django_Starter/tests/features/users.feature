Feature: User Management
  Scenario: Add a new user via UI
    Given I go to users page
    When I add a user "ui_user" with email "ui_user@example.com"
    Then I should see the user created in the UI