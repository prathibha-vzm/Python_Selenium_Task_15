* This directory contains code to test the webpage https://opensource-demo.orangehrmlive.com/web/index.php/auth/login .
* Username and password data sets are passed to run the valid and invalid credentials.
* Testing Architecture
* pytest, python selenium, exception conditions
* Framework Used - POM and Data Driven Testing Frame work 
* POM Structure:
1. Pages-> Under pages the elements are located and values are passed.
2. Test-> Test logic is done here. Read the data set from the spreadsheet(external file) and passed to the elements.
3. Utility -> Test_data file, Reading and Writing to the spreadhseet
4. Report -> HTML report generated is storeed here 
5. Screenshot-> To store the screenshots taken while test runs
* Data Driven Testing Framework:
1. Hardcoding is avoided
2. Stored the test data's in spreadsheet(Open Office) apart from the functions.
* conftest is to set the environment to run the test, to end the test and generate report with screenshot.
* pytest.ini to mark the test run.
* Note:
1. The ODS files may not be readable, so I have uploaded images of those sheets here.

