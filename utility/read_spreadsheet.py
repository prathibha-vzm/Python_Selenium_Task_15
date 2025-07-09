import pyexcel_ods3
#Importing to use the ods format spreadsheet

# This class read 2 sheets
class Spreadsheet:
    #Filename is stored in a variable
    def __init__(self):
        self.filename="C:/Users/91956/PycharmProjects/Task15&16/Data_Driven_Framework/utility/test_data.ods"
    #This method is to read the usernames and passwords in the spreadsheet
    def read_username_password(self):
        read_data=pyexcel_ods3.get_data(self.filename)  # To get the file
        sheet=read_data.get("credentials",[])  #To get the credentials sheet
        header=sheet[0]                        # marking the first row as header

        credential_list=[]                     # Creating an empty list to append username and password

        for row in sheet[1:]:                  # Looping through all rows starting from the second row
            datas=dict(zip(header,row))        # Zipping the header and its value, to get the needed columns later
            credential_list.append(datas)      # Appending the dictionary to the list
        return credential_list                 # returning the dictionary
    #This method is to read the url in dashboard assertion sheet
    def read_dashboard_url(self):
        read_data = pyexcel_ods3.get_data(self.filename)
        sheet = read_data.get("dashboard_assertion", [])
        urls = [row[0] for row in sheet[1:] if row]     #reading the url excluding the header
        return urls

    


