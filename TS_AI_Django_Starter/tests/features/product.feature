Feature: Product Management

  Scenario: Add a new product via UI
    Given I go to products page
    When I add a product "car" with price "100000"
    Then I should see the product created in the UI