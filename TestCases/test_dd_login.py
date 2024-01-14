import selenium.webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import Loggen
from Utilities import XLUtils

class TestCase_002:
    base_url = ReadConfig.getURL()
    path = ".//TestData//login.xlsx"
    logger = Loggen.logs()

    def test_HomePagetitle(self, setup):
        self.logger.info("----------------- TestCase_002 ----------------")
        self.logger.info("----------------- Verifying Home Page Title ---------------")
        self.driver = setup
        self.driver.get(self.base_url)
        page_title = self.driver.title

        if page_title == "Your store. Login":
            self.driver.close()
            self.logger.info("------------------ Home Page Title test is Passed -------------")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePagetitle.png")
            self.logger.error("------------------ Home Page Title test is Failed -----------")
            self.driver.close()
            assert False
            

    def test_Login(self, setup):
        self.logger.info("----------------- Verifying Login Page Title ---------------")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        list_status = []

        for row in range(2,self.rows+1):
            self.email = XLUtils.ReadData(self.path, "Sheet1", row, 1)
            self.password = XLUtils.ReadData(self.path, "Sheet1", row, 2)
            self.exp = XLUtils.ReadData(self.path, "Sheet1", row, 3)
            
            self.login_page.setEmail(self.email)
            self.login_page.setPassword(self.password)
    
            self.login_page.clickLogin()
            page_title = self.driver.title

            if "nopCommerce" in page_title:
                if self.exp == "Pass":
                    self.logger.info("------------------ Login Page Title test is Passed -------------")
                    list_status.append("Pass")
                    self.login_page.clickLogout()
                
                else:
                    self.logger.error("------------------ Login Page Title test is Failed -------------")
                    list_status.append("Fail")
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")

            elif "nopCommerce" not in page_title:
                if self.exp == "Pass":
                    self.logger.error("------------------ Login Page Title test is Failed -------------")
                    list_status.append("Fail")
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
                    self.login_page.clickLogout()
                else:
                    self.logger.info("------------------ Login Page Title test is Passed -------------")
                    list_status.append("Pass")

        if "Fail" in list_status:
            self.logger.error("------------ Data Driven Login test has been failed -------------")
            self.driver.close()
            assert False
        else:
            self.logger.info("------------ Data Driven Login test has been Passed -------------")
            self.driver.close()
            assert True
    