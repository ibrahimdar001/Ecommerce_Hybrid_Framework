from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    __email_textbox = "Email"
    __password_textbox = "Password"
    __login_button = "login-button"
    __link_logout_button = "Logout"


    def __init__(self, driver):
        self.driver = driver 

    def setEmail(self, username):
        self.driver.find_element(By.ID,self.__email_textbox).clear()
        self.driver.find_element(By.ID,self.__email_textbox).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.__password_textbox).clear()
        self.driver.find_element(By.ID,self.__password_textbox).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CLASS_NAME,self.__login_button).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.__link_logout_button).click()