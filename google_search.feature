Feature: Google Search Functionality

  Scenario: Search for India on Google
    Given I open the Chrome browser
    And I navigate to "https://www.google.com"
    When I type "India" in the search bar
    And I press Enter
    Then I take a screenshot of the search results
    And I close the browser