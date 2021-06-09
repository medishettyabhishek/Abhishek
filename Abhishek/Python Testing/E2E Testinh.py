from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

products = driver.find_elements_by_css_selector("div[class='card h-100']")

for product in products:
    Productname = product.find_element_by_xpath("div/h4/a").text
    if Productname == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_class_name("btn-primary").click()
driver.find_element_by_class_name("btn-success").click()

driver.find_element_by_id("country").send_keys('ind')

wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()

textmessage = driver.find_element_by_css_selector(".alert-success").text

assert "Success!" in textmessage

driver.get_screenshot_as_file("abhishek.png")