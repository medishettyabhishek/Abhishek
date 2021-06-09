from selenium.webdriver.common.by import By

from PageObjects.confirmPage import confirmpage


class checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    cardtitle = (By.CSS_SELECTOR, ".card-title a")
    cardfooter = (By.CSS_SELECTOR,".card-footer button")
    checkoutbutton = (By.CLASS_NAME , "btn-primary")
    confirmbutton = (By.CLASS_NAME,"btn-success")

    def getcardtites(self):
        return self.driver.find_elements(*checkoutpage.cardtitle)

    def getcardfooter(self):
        return self.driver.find_elements(*checkoutpage.cardfooter)

    def clickcheckout(self):
        return self.driver.find_element(*checkoutpage.checkoutbutton)

    def clickconfirmcheckout(self):
        self.driver.find_element(*checkoutpage.confirmbutton).click()
        ConfirmPage = confirmpage(self.driver)
        return confirmpage


