import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        options = Options()
        options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        #driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://nashik.ppbharti.in/")
    time.sleep(5)
    return driver

