from selenium.common import NoSuchElementException, TimeoutException # Importing Exceptions
from selenium.webdriver.common.by import By #Importing By to use the XPATH
from selenium.webdriver.support import expected_conditions #Importing this to use the explicit waits conditions
from selenium.webdriver.support.wait import WebDriverWait #WebDriverwait to wait statement

#  This class is to handle the error message that occurs with invalid credentials
class ErrorMessage:
    #Declaring all the variables in constructor, Locators and wait with 10seconds timeout
    def __init__(self,driver):
        self.driver=driver
        self.credential_error_message=(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.wait=WebDriverWait(driver,10)
    #This method to locate the error message adn validating as valid or invalid credentials
    def get_error_message(self):
        try:
            err_msg = self.wait.until(expected_conditions.visibility_of_element_located(self.credential_error_message))
            #error_message = err_msg.text
            if err_msg:
                print("Invalid Credentials")
        except (NoSuchElementException,TimeoutException):
            print("Valid Credentials")

