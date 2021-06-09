
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()