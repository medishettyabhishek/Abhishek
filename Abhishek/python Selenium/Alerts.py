from selenium import webdriver
from selenium.webdriver.support.select import Select
validatetext = "option3"
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

driver.find_element_by_css_selector("#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
assert validatetext in alerttext
alert.accept()

driver.close()