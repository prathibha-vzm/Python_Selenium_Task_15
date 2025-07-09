from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, TimeoutException # Importing Exceptions
from selenium.webdriver.common.by import By #Importing By to use the XPATH
from selenium.webdriver.support import expected_conditions #Importing this to use the explicit waits conditions
from selenium.webdriver.support.wait import WebDriverWait #WebDriverwait to wait statement

# This class contains all the elements in login page
class Login:
    #Declaring all the variables in constructor, Locators and wait with 10seconds timeout
    def __init__(self,driver):
        self.driver=driver
        self.username_input_box=(By.XPATH,"//input[@placeholder='Username']")
        self.password_input_box=(By.XPATH,"//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.wait=WebDriverWait(driver,10)
    #This method is to enter the username in the particular input box located and validating the box is enabled and clear with exceptions handling
    def enter_username(self,username):
        username_input=self.wait.until(expected_conditions.visibility_of_element_located(self.username_input_box))
        try:
            if username_input.is_enabled():
                username_input.clear()
                if username:
                   username_input.send_keys(username)
        except (ElementNotInteractableException,ValueError):
            print("Email Input is not found/No value passed")
    #This method is to enter the password in the particular input box located and validating the box is enabled and clear with exceptions handling
    def enter_password(self,password):
        password_input=self.wait.until(expected_conditions.visibility_of_element_located(self.password_input_box))
        try:
            if password_input.is_enabled():
                password_input.clear()
                if password:
                    password_input.send_keys(password)
        except (ElementNotInteractableException, ValueError):
            print("Password Input is not found/No value passed")
    # This method is to click on login button and exceptions that might occur is handled
    def click_login(self):
        try:
            login = self.wait.until(expected_conditions.element_to_be_clickable(self.login_button))
            login.click()
            print("\nLogin button clicked successfully.")
        except (ElementClickInterceptedException,TimeoutException):
            print("ElementClickInterceptedException")








