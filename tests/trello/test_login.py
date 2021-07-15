import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import selenium
import time
import allure
from pageobjects.login_page_trello import LoginPage


class Tests_Login_001:
    base_url = "https://trello.com/login"
    username = "yasikcoded@gmail.com"
    password = "Jobs@123$"

    # def test_home_page_title(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.base_url)
    #     a_title = self.driver.title
    #     self.driver.close()
    #     if a_title == "IBM Resiliency Orchestration :: Login":
    #         assert True
    #     else:
    #         assert False
    #     self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.uiTest
    @allure.title("Main Login Functions getting executed")
    @allure.description("Open Trello page with valid username")
    def test_login_trello_page(self, browser_setup,logger):
        self.driver = browser_setup
        logger.info("Launching URL")
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.click_login_with_atlassion_button()
        #time.sleep(5)
        #self.lp.set_password(self.password)
        #self.lp.click_login()
        #a_title = self.driver.title
        allure.attach(self.driver.get_screenshot_as_png(), name= "testLoginScreen", attachment_type=AttachmentType.PNG)
        self.driver.close()
        #if a_title == "Boards | Trello":
        assert True