from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import Loggen

class TestCase_001:
    base_url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = Loggen.logs()

    def test_HomePagetitle(self, setup):
        self.logger.info("----------------- TestCase_001 ----------------")
        self.logger.info("----------------- Verifying Home Page Title ---------------")
        self.driver = setup
        self.driver.get(self.base_url)
        page_title = self.driver.title

        if page_title == "Your store. Login":
            assert True
            self.logger.info("------------------ Home Page Title test is Passed -------------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_HomePagetitle.png")
            self.logger.info("------------------ Home Page Title test is Failed -----------")
            self.driver.close()
            assert False
            

    def test_Login(self, setup):
        self.logger.info("----------------- Verifying Login Page Title ---------------")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = Login(self.driver)
        self.login_page.setEmail(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        page_title = self.driver.title

        if "nopCommerce" in page_title:
            assert True
            self.logger.info("------------------ Login Page Title test is Passed -------------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_Login.png")
            self.logger.info("------------------ Login Page Title test is Failed -------------")
            self.driver.close()
            assert False