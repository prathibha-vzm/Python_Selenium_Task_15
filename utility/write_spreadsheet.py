import pyexcel_ods3 #Importing to use the ods format spreadsheet
#This class is to write the test-report in spreadsheet
class WriteSheet:
    def __init__(self): #storing the file path
        self.filename="C:/Users/91956/PycharmProjects/Task15&16/Data_Driven_Framework/utility/test_data.ods"
    #This method's parameters are to write on the spreadsheet
    def write_report(self,sheet_name,row_number,date,time,tester_name,test_result):
        read_data = pyexcel_ods3.get_data(self.filename) # TO find the file
        sheet = read_data.get("credentials", [])  #To find the sheet
        header = sheet[0]                         #Marking the header value

        #Marking the index value by column name from sheet and passing it through variables
        date_column=header.index("Date")
        time_column=header.index("Time_of_Test")
        name_column=header.index("Name_of_Tester")
        result_column=header.index("Test_Result")

        #defining the index value to append the values
        row_number=int(row_number)
        write_to_row=row_number+1

        #To check the sheet has defined(passing parameters) columns
        while len(sheet) <= write_to_row:
            sheet.append([""] * len(header))

        # Ensure the row has enough columns
        while len(sheet[write_to_row]) < len(header):
            sheet[write_to_row].append("")

        #Appending the values to the rows that column name matches
        sheet[write_to_row][date_column]=date
        sheet[write_to_row][time_column]=time
        sheet[write_to_row][name_column]=tester_name
        sheet[write_to_row][result_column]=test_result

        #Storing all the value to the sheet
        read_data[sheet_name]=sheet
        pyexcel_ods3.save_data(self.filename,read_data) # saving the updated sheet
