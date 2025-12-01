Feature: Authentication - Sign Up Functionality
  As a new user
  I want to be able to create an account
  So that I can register on the platform

  Background:
    Given I am on the Elite Shoppy home page

  Scenario: Successful sign up with valid data
    When I click on the Sign Up button
    And I fill the sign up form with valid data:
      | name            | email              | password    | confirmPassword |
      | New Test User   | newuser@test.com   | Pass12345   | Pass12345       |
    And I click the Sign Up submit button
    Then I should see a registration success message

  Scenario: Sign up modal opens correctly
    When I click on the Sign Up button
    Then the Sign Up modal should be displayed
    And the Sign Up modal should contain Name field
    And the Sign Up modal should contain Email field
    And the Sign Up modal should contain Password field
    And the Sign Up modal should contain Confirm Password field
    And the Sign Up submit button should be enabled

  Scenario: Sign up with empty fields
    When I click on the Sign Up button
    And the Sign Up modal should be displayed
    And I clear the sign up form
    And I click the Sign Up submit button
    Then the Sign Up form should show validation errors

  Scenario: Sign up with mismatched passwords
    When I click on the Sign Up button
    And I fill the sign up form with mismatched passwords:
      | name            | email              | password    | confirmPassword |
      | Test User       | testuser@test.com  | Pass12345   | Pass54321       |
    And I click the Sign Up submit button
    Then I should see password mismatch error

  Scenario: Sign up with invalid email
    When I click on the Sign Up button
    And I enter invalid email "invalidemail" in Sign Up form
    Then I should see email validation error in Sign Up modal

  Scenario: Sign up with weak password
    When I click on the Sign Up button
    And I fill the sign up form with weak password:
      | name            | email              | password    | confirmPassword |
      | Test User       | testuser@test.com  | 123         | 123             |
    Then I should see password strength warning

  Scenario: Sign up modal can be closed
    When I click on the Sign Up button
    And the Sign Up modal should be displayed
    And I close the Sign Up modal
    Then the Sign Up modal should not be displayed
