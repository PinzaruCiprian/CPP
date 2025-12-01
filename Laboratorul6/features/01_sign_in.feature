Feature: Authentication - Sign In Functionality
  As a user
  I want to be able to sign in to the platform
  So that I can access my account

  Background:
    Given I am on the Elite Shoppy home page

  Scenario: Successful sign in with valid credentials
    When I click on the Sign In button
    And I fill the login form with valid data:
      | name            | email              |
      | Test User       | testuser@test.com  |
    And I click the Sign In submit button
    Then I should see a success message

  Scenario: Sign in modal opens correctly
    When I click on the Sign In button
    Then the Sign In modal should be displayed
    And the Sign In modal should contain Name field
    And the Sign In modal should contain Email field
    And the Sign In submit button should be enabled

  Scenario: Sign in with empty fields
    When I click on the Sign In button
    And I clear the login form
    And I click the Sign In submit button
    Then the Sign In form should show validation errors

  Scenario: Sign in with invalid email format
    When I click on the Sign In button
    And I enter invalid email "invalidemail@test" in Sign In form
    Then I should see email validation error

  Scenario: Sign in modal can be closed
    When I click on the Sign In button
    And the Sign In modal should be displayed
    And I close the Sign In modal
    Then the Sign In modal should not be displayed
