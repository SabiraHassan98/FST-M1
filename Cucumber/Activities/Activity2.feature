@activity2

Feature: Activity to test the feature

Scenario: Testing Login
	Given the user is on the login page
	When the user enters username and password
	And clicks the submit button
	Then  get the confirmation message and verify it