from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://trade.angelbroking.com/Login")

driver.find_element_by_id("txtUserID").send_keys("A234592")
driver.find_element_by_css_selector("input[id='txtTradingPassword']").send_keys("Medishetty")
driver.find_element_by_id("loginBtn").click()


