import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(5) #driver will max wait for 5 seconds if page loads before that then it skips time and move on

driver.find_element_by_class_name("search-keyword").send_keys("ber")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
#//div[@class='product-action']/button/parent::div/parent::div/h4
veggies = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for items in veggies:
    print(items.find_elements_by_xpath("parent::div/parent::div/h4").text)
    items.click()

driver.find_element_by_css_selector("img[alt ='Cart']").click()
driver.find_element_by_xpath("//button[text() ='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector(".promoInfo").text)

