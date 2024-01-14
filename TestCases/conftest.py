from selenium import webdriver
import pytest
import pytest_metadata
from pytest_metadata.plugin import metadata_key

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


# This is a hook that will set up environment for HTML report

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "NoP Commerce"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Ibrahim"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
