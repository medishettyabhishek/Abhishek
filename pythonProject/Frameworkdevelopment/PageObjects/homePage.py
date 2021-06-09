from selenium.webdriver.common.by import By

from PageObjects.checkoutpage import checkoutpage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    tickbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    finalsbubmit = (By.CSS_SELECTOR, "input[class*='btn-success']")
    Alertmessage =(By.CSS_SELECTOR,"div[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        CheckOutPage = checkoutpage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def gettickbox(self):
        return self.driver.find_element(*HomePage.tickbox).click()

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getfinalsubmitbutton(self):
        return self.driver.find_element(*HomePage.finalsbubmit).click()

    def getsubmitmesssage(self):
        return self.driver.find_element(*HomePage.Alertmessage).text
