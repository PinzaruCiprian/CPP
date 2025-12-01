Feature: Test Mens Page

  Background:
    Given I navigate to the Mens page

  @smoke @normal
  Scenario: TC1 - Test page loads correctly
    Given the Mens page is loaded completely
    When I wait for page to load
    Then the page should load within 3 seconds
    And all main elements should be visible:
      | element    |
      | title      |
      | products   |
      | header     |
      | footer     |
    And product images should be loaded
    And CSS and JS resources should be available

  @high
  Scenario: TC2 - Test navigation menu functionality
    Given the navigation menu is visible
    When I hover over each menu item
    Then each menu item should respond to hover
    And when I click on "Home" link
    Then I should be redirected to home page
    And when I click on "Womens" link
    Then I should be redirected to womens page
    And when I click on "Mens" link
    Then I should stay on mens page
    And no 404 or 500 errors should appear

  @normal
  Scenario: TC3 - Test product display in Mens section
    Given products from Mens category are loaded
    When I scroll to products section
    Then each product should display:
      | attribute   |
      | image       |
      | title       |
      | price       |
      | action_btn  |
    And product data should be correctly fetched from database
    And product graphic consistency should be maintained

  @low @failed
  Scenario: TC4 - Test Contact link in footer
    Given the footer is visible
    When I scroll to footer section
    And I click on "Contact" link
    Then I should be redirected to contact page
    And no broken links should occur
    And response time should be acceptable

  @high
  Scenario: TC5 - Test page responsiveness
    Given the Mens page is loaded
    When I view page on desktop (1920x1080)
    Then all elements should be visible without horizontal scroll
    And layout should be correct
    When I resize to tablet (768x1024)
    Then layout should adapt correctly
    And menu should remain accessible
    And no overlapping elements
    When I resize to mobile (375x667)
    Then vertical scroll should work smoothly
    And touch interactions should be accessible
    And buttons should be properly sized for touch

  @high @failed
  Scenario: TC6 - Test search functionality
    Given the search bar is visible and active
    When I enter "shirt" in search field
    And I press Enter or click Search button
    Then search results should display relevant products
    And no "Page not Found" error should occur
    And search response time should be reasonable
