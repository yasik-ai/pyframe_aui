class _Const(object):

    """slots_allows you to explicitly state which instance attributes you expect your object instances
     to have, with the expected results"""

    __slots__ = ()

    # Driver and Browser Configuration
    VIRTUAL_ENV_PATH = "venv/lib/python3.8/site-packages/"
    CHROME_DRIVER_PATH = "chromedriver_py/chromedriver_mac64"
    BROWSER_CHROME = "chrome"
    BROWSER_FIREFOX = "firefox"
    BROWSER_IE = "ie"
