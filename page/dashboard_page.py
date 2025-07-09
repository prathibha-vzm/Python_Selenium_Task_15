from selenium.common import TimeoutException, NoSuchElementException # Importing Exceptions
from selenium.webdriver.common.by import By #Importing By to use the XPATH
from selenium.webdriver.support import expected_conditions #Importing this to use the explicit waits conditions
from selenium.webdriver.support.wait import WebDriverWait #WebDriverwait to wait statement

#Creating this Dashboard class
# 1. to load the page,
# 2.Then to read the user_name(Logged in persons name),
# 3.Then the time of logged in details in the webpage
class Dashboard:
    #Declaring all the variables in constructor, Locators and wait with 10seconds timeout
    def __init__(self,driver):
        self.driver=driver
        self.dashboard = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        self.wait = WebDriverWait(driver, 10)
        self.user_name=(By.XPATH,"//p[@class='oxd-userdropdown-name']")
        self.time_date=(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-attendance-card-details']")
    #This method helps to load the dashboard page once login is clicked, and handling the exceptions that might occur
    def view_dashboard(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.dashboard))
            print("Dashboard Loaded")
        except (TimeoutException,AssertionError):
            print("Dashboard Not Loaded")
    #This method is to locate the logged in name, and handling the exceptions that might occur
    def find_user_name(self):
        try:
            user=self.wait.until(expected_conditions.visibility_of_element_located(self.user_name))
            user_text=user.text
            print(f"Logged in {user_text}")
        except (NoSuchElementException,TimeoutException):
            print("Username not found")
    #This method is to locate the logged in time, and handling the exceptions that might occur
    def find_time_date(self):
        try:
            time_date=self.wait.until(expected_conditions.visibility_of_element_located(self.time_date))
            time_date_text=time_date.text
            print(f"Logged In Time {time_date_text}")
        except (NoSuchElementException,TimeoutException):
            print("Date and Time Not found")