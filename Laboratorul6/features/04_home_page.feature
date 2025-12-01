Feature: Home Page Functionality
  As a user
  I want to interact with the home page
  So that I can browse products and features

  Background:
    Given I am on the Elite Shoppy home page

  Scenario: Home page loads correctly
    Then the home page should be loaded successfully
    And Sign In button should be visible
    And Sign Up button should be visible
    And Cart button should be visible

  Scenario: Navigate to products
    When I click on the Cart button
    Then the page should display products

  Scenario: Community poll interaction
    When I select a poll option
    And I submit the poll
    Then the poll should be submitted successfully

  Scenario: Browse products
    Then at least one product should be visible
    When I click on a product Quick View button
    Then the product details should be displayed

  Scenario: Sort products
    When I sort products by "Name(A - Z)"
    Then products should be sorted correctly
