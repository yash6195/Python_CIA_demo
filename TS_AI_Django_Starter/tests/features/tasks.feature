Feature: Task Management

  Scenario: Add a new task via UI
    Given I go to tasks page
    When I add a task with title "sell cars"
    Then I should see the task created in the UI