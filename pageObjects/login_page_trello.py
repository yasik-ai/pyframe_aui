from selenium import webdriver
import selenium
import allure
from driverfactory.driverfactory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from commonUtils.fileUtils import FileUtils


class LoginPage:
    textbox_email_id = "user"
    btn_login_atlassian_id = "login"
    textbox_password_xpath = "//div[@class]/input[@id='password'"
    btn_login_xpath = "//button[@id='login-submit']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        FileUtils.logger().info("Enter User name for login")
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)

    def click_login_with_atlassion_button(self):
        FileUtils.logger().info("Clicking on login with Atlassion account button")
        element_present = EC.element_to_be_clickable((By.ID, self.btn_login_atlassian_id ))
        wait(self.driver, 10).until(element_present)
        self.driver.find_element_by_id(self.btn_login_atlassian_id).click()

    def set_password(self, password):
        wait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.textbox_password_xpath)))
        self.driver.find_element_by_id(self.textbox_password_xpath).clear()
        self.driver.find_element_by_id(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()