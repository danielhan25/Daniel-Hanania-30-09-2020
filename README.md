# Daniel-Hanania-30-09-2020
Automation framework

This was build in python and selenium server.


I have two base objects which are SeleniumDriver,WebDriverFactory

WebDriverFactory - Responsible for the webDriver instance. you can run the test 
on any browser you would like.
command on terminal:
"py.test -s -v tests/home/home_page_tests.py --browser chrome"

SeleniumDriver - Responsible on all the functions that the page elements could do.
for example:elementClick,sendKeys,clearKeys

I have two utilities objects which are customLogger,TestStatus

customLogger - Responsible for creating log file and append each action
we do on the tests

TestStatus - Responsible for marking the asserts in each tests case and give final assertion if the tests is failed or succeeded


I have two page object homePage,thankYouPage

homePage - have 3 input elements: name,email,phone and 1 send button,
also 3 error messages which help us to verify the tests

thankYouPage - has label of "Thank you" which we verify is loaded after we enter all the requirements on homePage


there is one test file which include 5 tests:

1. trying to click send without any information
2. trying to click send with just name
3. trying to click send with just email
4. trying to click send with just phone
5. entering all the requirements and opening the thank you page

This is also the running order of the tests 1-5
