import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("browser_name")
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    elif browsername == "firefox":
        driver = webdriver.Chrome(executable_path="c:\\geckodriver.exe")
    elif browsername == "IE":
        driver = webdriver.Chrome(executable_path="c:\\IEDriverServer.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
