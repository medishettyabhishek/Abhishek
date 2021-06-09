from selenium.webdriver.common.by import By


class confirmpage:

    def __init__(self, driver):
        self.driver = driver

    sendkeys = (By.ID, "country")
    textmessage = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirmbutton =(By.CSS_SELECTOR,"input[type='submit']")
    finalmessage = (By.CSS_SELECTOR, ".alert-success")

    def SendKeys(self):
        return self.driver.find_element(*confirmpage.sendkeys)

    def TextMessage(self):
        return self.driver.find_element(*confirmpage.textmessage)

    def clickcheckbox(self):
        return self.driver.find_element(*confirmpage.checkbox)

    def clickconfirm(self):
        return self.driver.find_element(*confirmpage.confirmbutton)

    def checkfinalmessage(self):
        return self.driver.find_element(*confirmpage.finalmessage)

