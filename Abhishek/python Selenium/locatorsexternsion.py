from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_css_selector("#username").send_keys("abhishek")
driver.find_element_by_css_selector('.password').send_keys("bqwubbki")
driver.find_element_by_css_selector('.password').clear()

driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()



