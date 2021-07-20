from selenium import webdriver
from pytest import fixture
import os
import sys
import logging
import time
from driverfactory.driverfactory import DriverFactory
from commonutils.fileUtils import FileUtils
from tests.config import Config


@fixture
def browser_setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--start-maximized")
    chrome_path = "/Users/mohamedyasik/Automation/Python/pyframe_aui/venv/lib/python3.8/site-packages/chromedriver_py/chromedriver_mac64"
    driver = webdriver.Chrome(executable_path=chrome_path,
                              options=options)
    return driver


# @fixture(autouse=True, scope='package')
# def cleanup_old_report():
#     reports_folder = "reports/latest_reports"
#     report_path = os.path.abspath(reports_folder)
#     archived_folder = "reports/archived_reports"
#     archived_fpath = os.path.abspath(archived_folder)
#     print(archived_fpath)
#     print("Copying the old reports to archived folder")
#     FileUtils.copy_and_move_files_to_other_folder(report_path + "/", archived_fpath + "/")
#     print("Cleaning the older report")
#     os.system('allure generate --clean --output ' + report_path)
#     yield
#     print("\nTearing Down")


@fixture()
def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    yield logger


# def pytest_sessionfinish(session, exitstatus):
#     """Called after whole test run finished, right before
#         returning the exit status to the system. """
#     reports_folder = "reports/latest_reports/"
#     print("Generating Allure Reports")
#     report_path = os.path.abspath(reports_folder)
#     os.system('\nallure serve ' + report_path)


def pytest_addoption(parser):
    """It is a arg parser which is not required to import and will act a configuration file
    set default = qa , it will pick only qa environment, or else
    add command line --env qa"""
    parser.addoption(
        "--env",
        action="store",
        help="Environment to create and run during execution"
    )


@fixture(scope='session')
def env(request):
    """ Method to fetch and return values from config files from env property"""
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    """ To run on multiple browser """
    driver = request.param
    b_driver = driver()
    yield b_driver
    b_driver.quit()

# @pytest.fixture
# def setup():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-ssl-errors=yes')
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument("--start-maximized")
#    chrome_path = "/Users/mohamedyasik/Automation/Python/pyframe_aui/venv/lib/python3.8/site-packages/chromedriver_py/chromedriver_mac64"
#     driver = webdriver.Chrome(executable_path=chrome_path,
#                               options=options)
#     return driver
#
#
# @pytest.fixture
# def oneTimeSetup(browser):
#     print("Running One Time Setup")
#     wdf = DriverFactory(browser)
#     driver = wdf.get_driver()
#
#     yield driver
#     driver.quit()
#     print("Running one time tearDown")
