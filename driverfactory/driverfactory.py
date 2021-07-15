from selenium import webdriver
from commonutils.constants import _Const as CONST


class DriverFactory:

    def __init__(self, browser_name):
        self.browser = browser_name

    def get_driver(self):
        if CONST.BROWSER_CHROME == self.browser_name:
            driver = DriverFactory.set_chromedriver()
        elif CONST.BROWSER_FIREFOX == self.browser_name:
            pass
        elif CONST.BROWSER_IE == self.browser_name:
            pass
        else:
            raise Exception(
                "Driver name {} must be configured in Environment configuration file".format(self.browser_name))
        return driver

    @staticmethod
    def shutdown():
        DriverFactory.get_driver().quit()

    @staticmethod
    def set_chromedriver():
        """Description: Setting up executable path to chrome and configure browser
           Parameter: pass application site as url
           Return:    """

        chrome_options = DriverFactory.build_chrome_options()
        chrome_path = CONST.VIRTUAL_ENV_PATH + CONST.CHROME_DRIVER_PATH
        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        return driver

    @staticmethod
    def build_chrome_options():
        """ Configure chrome options with chrome driver
            Parameter: None
            Return: chrome option       """

        chrome_option = webdriver.ChromeOptions()
        chrome_option.accept_untrusted_certs = True
        chrome_option.assume_untrusted_cert_issuer = True
        chrome_option.add_argument("--disable-popup-blocking")
        chrome_option.add_argument("--ignore-certificate-errors")
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument('--disable-infobars')
        chrome_option.add_argument('--disable-logging')
        chrome_option.add_argument("--disable-notifications")
        chrome_option.add_argument('--ignore-ssl-errors=yes')
        chrome_option.add_argument('--ignore-certificate-errors')
        return chrome_option
