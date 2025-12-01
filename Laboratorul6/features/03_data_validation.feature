Feature: Data Validation
  As a system
  I want to validate all user input data
  So that data integrity is maintained

  Background:
    Given I am on the Elite Shoppy home page

  Scenario: Validate email format
    When I validate email "validuser@example.com"
    Then the email should be valid
    When I validate email "invalid.email"
    Then the email should be invalid

  Scenario: Validate name format
    When I validate name "John Doe"
    Then the name should be valid
    When I validate name "J"
    Then the name should be invalid

  Scenario: Validate password strength
    When I validate password "StrongPass123"
    Then the password should be strong
    When I validate password "weak"
    Then the password should be weak

  Scenario: Email field validation in Sign In form
    When I click on the Sign In button
    And I enter text "invalidemail" in Sign In email field
    Then an email validation message should appear

  Scenario: Name field validation in Sign Up form
    When I click on the Sign Up button
    And I enter text "A" in Sign Up name field
    Then a name validation message should appear

  Scenario: Password matching validation in Sign Up
    When I click on the Sign Up button
    And I enter password "Password123" in Sign Up password field
    And I enter password "Password456" in Sign Up confirm password field
    Then a password mismatch message should appear

  Scenario: All required fields validation
    When I click on the Sign Up button
    And I try to submit without filling any field
    Then validation errors should be shown for all required fields
