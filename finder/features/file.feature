Feature: Email Finder module

        Background:
        When  I click on the linktext "Email Finder"

        # Scenario: Validate the user can able to find emails using Valid First name, last name and domain name
        #          When I add "prathyusha" using placeholder "First Name"
        #          And  I add "siripothu" using placeholder "Last Name"
        #          And  I add "500apps.com" into the inputfield using the id "input-domain"
        #          And  I click on the button using the text "Find"
        #         When  I wait for the element "//span[normalize-space()='Clear All']" with in "5" seconds
        #         Then  I expect that the element contains text "prathyusha.siripothu@500apps.com" is vissible
        #          And  I expect that the element contains text "100%" is vissible
        #          And  I expect that the element contains text "Email exists" is vissible

        # Scenario: Validate the user can able to find emails using Invalid Details
        #         When I add "venky" using placeholder "First Name"
        #         And  I add "cash" using placeholder "Last Name"
        #         And  I add "500apps.com" into the inputfield using the id "input-domain"
        #         And  I click on the button using the text "Find"
        #         When I wait for the element "//span[normalize-space()='Clear All']" with in "5" seconds
        #         Then I expect that the element contains text "venky.cash@500apps.com" is vissible
        #         And  I expect that the element contains text "100%" is vissible
        #         And  I expect that the element contains text "Cannot find any combinations. Perhaps, the lead does not exist." is vissible

        # Scenario: Validate the user can use the clear all button in Email finder
        #         When  I add "prathyusha" using placeholder "First Name"
        #          And  I add "siripothu" using placeholder "Last Name"
        #          And  I add "500apps.com" into the inputfield using the id "input-domain"
        #          And  I click on the button using the text "Find"
        #         When  I wait for the element "//span[normalize-space()='Clear All']" with in "10" seconds
        #         Then  I expect that the element contains text "prathyusha.siripothu@500apps.com" is vissible
        #         When  I click on textlink "Save"
        #         And   I click on linktext "Create New"
        #         And   I pass data "venky" into list name field in "email-finder" Add to List popup
        #         And   I click on "Add to List" label "Create List" button with index number "4"
        #         And   I click on button using text "Save"
        #         And   I scroll till the page up
        #         When  I wait for the element "//a[normalize-space()='Lists']" with in "5" seconds
        #         And   I click on textlink " Lists "
        #         And   I click on linktext " venky "
        #         Then  I expect that  the element contains text " 500apps.com " is visible
        #         Then  I expect that the element contains text "Email Finder" is visible
        #         When  I click on the "Delete" icon in contacts
        #         And   I click on button using text "Confirm"
        #         When  I click on the "Delete" icon in a row
        #         And   I click on button using text "Confirm"
        #         Then  I expect that the element with text "venky" does not exist "yes"

        # Scenario: Validate the user can able to upload the csv file and verify the search results in the bulk email finder
        #         When I click on element contains text " Switch to Bulk Email Finder"
        #         And  I upload file "Bulkfind50.csv" in "finder" app using class "file-input"
        #         And  I wait for the element "//button[normalize-space()='Export']" with in "30" seconds
        #         Then I expect that element contains text "Export" is visible
        #         And  I expect that element contains text "Search Results" is visible
        #         Then I verified the count of the emails "25" using the element "//tbody//tr"

        # Scenario: Validate the user can able to add a success email to the list from the bulk email finder
        #         When I click on element contains text " Switch to Bulk Email Finder"
        #         And  I upload file "Bulkfind50.csv" in "finder" app using class "file-input"
        #         And  I wait for the element "//button[normalize-space()='Export']" with in "30" seconds
        #         Then I expect that element contains text "Export" is visible
        #         When I click on textlink "Save"
        #         And  I click on linktext "Create New"
        #         And  I pass data "venky" into list name field in "email-finder" Add to List popup
        #         And  I click on "Add to List" label "Create List" button with index number "4"
        #         And  I click on button using text "Save"
        #         And  I scroll till the page up
        #         And  I wait for the element "//a[normalize-space()='Lists']" with in "5" seconds
        #         And  I click on textlink " Lists "
        #         And  I click on linktext " venky "
        #         Then I expect that the element contains text "Email Finder" is visible
        #         When I click on the "Delete" icon in contacts
        #         And  I click on button using text "Confirm"
        #         When I click on the "Delete" icon in a row
        #         And  I click on button using text "Confirm"
        #         Then I expect that the element with text "venky" does not exist "yes"

        # Scenario: Validate the user can click on Reset button in the bulk email finder
        #         When I click on element contains text " Switch to Bulk Email Finder"
        #         And  I upload file "Bulkfind50.csv" in "finder" app using class "file-input"
        #         And  I wait for the element "//button[contains(text(),'Export')]" with in "30" seconds
        #         And  I click on button "Reset"
        #         Then I expect that element with text "Bulkfind50" does not exist "yes"

        # Scenario: Validate the user can add email to CRM apps in Email finder
        #         When I add "prathyusha" using placeholder "First Name"
        #         And  I add "siripothu" using placeholder "Last Name"
        #         And  I add "500apps.com" into the inputfield using the id "input-domain"
        #         And  I click on the button using the text "Find"
        #         When I wait for the element "//span[normalize-space()='Clear All']" with in "5" seconds
        #         And  I wait for the element "//td[normalize-space()='Save']" with in "5" seconds
        #         When I click on the linktext "Save"
        #         And  I click on the button text "Agile CRM"
        #         And  I wait for element "//td[normalize-space()='Save']" with in "1" seconds
        #         And  I click on the button having text "Save"
        #         And  I wait for the element "//h4[normalize-space()='Add to CRM']" with in "10" seconds
        #         Then I expect that element with text "Add to Agile CRM" does not exist "yes"