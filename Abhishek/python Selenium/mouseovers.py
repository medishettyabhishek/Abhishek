from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
childmenu = driver.find_element_by_link_text("Top")
action.move_to_element(childmenu).click()