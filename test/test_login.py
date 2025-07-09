from datetime import datetime #To use the date and time methods
import pytest #Pytest to use the mark and parametrize
# Class pages are imported
from Data_Driven_Framework.page.dashboard_page import Dashboard
from Data_Driven_Framework.page.login_error_page import ErrorMessage
from Data_Driven_Framework.page.login_page import Login
from Data_Driven_Framework.utility.read_spreadsheet import Spreadsheet
from Data_Driven_Framework.utility.write_spreadsheet import WriteSheet

#This is to read the spreadsheets
spreadsheet=Spreadsheet() #Created object for the Spreadsheet class
credential_list=spreadsheet.read_username_password()  #TO read Username and password method is called
dashboards_url=spreadsheet.read_dashboard_url()  #to read url method is called
test_data=[] #creating an empty list to store usernames and passwords and enumerate it accordingly
for i,data in enumerate(credential_list): #For loop with enumerate is used to read username and password in data dict and to get index
    test_data.append((data['Username'],data['Password'],i)) # appending all to a tuple

#This is the spreadsheet to write the report
write_back=WriteSheet()

#Marked as sanity, 2 parameters are sent here, 1 for dashboard_url, and test_data tuple
@pytest.mark.sanity
@pytest.mark.parametrize("expected_url",dashboards_url)
@pytest.mark.parametrize("username_data,password_data,row_number",test_data)
def test_login_process(set_up,username_data,password_data,row_number,expected_url):
    #creating object for the class and calling its method
    driver=set_up
    login=Login(driver)
    login.enter_username(username_data)
    login.enter_password(password_data)
    login.click_login()
    actual_url = driver.current_url #Fetching the current page url once clicked on log in
    invalid_credentials = ErrorMessage(driver)
    invalid_credentials.get_error_message()   # looking for the error message that might appear on invalid credentials
    dashboard_obj=Dashboard(driver)           # If not the dashboard page will open
    dashboard_obj.view_dashboard()
    if actual_url == expected_url:            #validating the login with dashboard URL
        print("Assertion Passed")
        result = "Valid Credentials"          #Since true, Valid credential passed through result
        dashboard_obj.find_user_name()        # Fetching the name, date and time in the dashboard
        dashboard_obj.find_time_date()
    else:
        print("Assertion Error")            # When the credentials are false, this will work
        result = "Invalid Credentials"      # Passing the result with the message Invalid

    current_date = datetime.now().strftime("%Y-%m-%d")  #To get the test running time datetime now is used and only date format is stored here
    current_time = datetime.now().strftime("%H:%M:%S")  #To get the test running time datetime now is used and only date format is stored here

    write_back.write_report(sheet_name="credentials",   #Passing all the values to the Write method that write on existing spreadsheet
                            row_number=row_number,
                            date=current_date,
                            time=current_time,
                            tester_name="Prathibha",
                            test_result=result)









