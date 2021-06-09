from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/frames")
driver.implicitly_wait(5)

driver.find_element_by_link_text("iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("hello i am medishetty abhishek")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h3').text)
