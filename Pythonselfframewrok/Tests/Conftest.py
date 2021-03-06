import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
