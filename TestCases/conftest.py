from selenium import webdriver
import pytest

@pytest.fixture
def setup(browser):
    if browser == 'Chrome' or browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox' or browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver

# This will get value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return browser value for setup driver
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")