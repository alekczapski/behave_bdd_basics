Feature: Healthy food

  Scenario Outline: eating
    Given there were <amount> cucumbers
    When I eat <eaten> cucumbers
    Then I should have <left> cucumbers

    Examples:
      | amount | eaten | left |
      |      5 |     2 |    3 |
      |      3 |     3 |    0 |
      |      0 |     0 |    0 |
