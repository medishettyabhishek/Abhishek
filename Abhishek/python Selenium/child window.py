from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
#parentwindow = driver.window_handles[0]
childwinodw = driver.window_handles[1]
driver.switch_to.window('childwinodw')
print(driver.find_element_by_tag_name("h3").text)
