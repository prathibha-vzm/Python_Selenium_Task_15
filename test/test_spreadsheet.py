from Data_Driven_Framework.utility.read_spreadsheet import Spreadsheet
# This is to check the username and password , dashboard_url are fetched and printed here
def test_spreadsheet_data():
    spreadsheet=Spreadsheet()
    credential_list=spreadsheet.read_username_password()
    for data in credential_list:
        print(f"Username--{data['Username']} Password--{data['Password']}")
    dashboard_url=spreadsheet.read_dashboard_url()
    print(dashboard_url)
