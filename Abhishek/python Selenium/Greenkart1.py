import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list = []
list2 = []
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element_by_css_selector("img[alt ='Cart']").click()
driver.find_element_by_xpath("//button[text() ='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 6)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies = driver.find_elements_by_css_selector("p.product-name")
for items in veggies:
    list2.append(items.text)

print(list2)

assert list == list2

orginalamount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

discountamount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountamount) < int(orginalamount)
print(driver.find_element_by_css_selector(".promoInfo").text)
