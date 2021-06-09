from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

driver.find_element_by_id("displayed-text").is_displayed()
