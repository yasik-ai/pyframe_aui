from pytest import mark

@mark.explore
def test_environment_qa(app_config):
    b_url = app_config.base_url
    port = app_config.app_port
    browser = app_config.browser
    assert b_url == 'https://myqa-env.com'
    assert port == 8443
    assert browser == 'chrome'

@mark.skip(reason = "deployment is not available")
@mark.explore
def test_environment_dev(env):
    assert env == 'dev'

@mark.xfail(reason="Environment build is not available")
@mark.explore
def test_not_implemented_yet(env):
    assert  env == 'inprogress'

@mark.explore
def test_open_url(browser):
    browser.get("https://www.bmw.in/en/index.html")
