import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.checkoutpage import checkoutpage
from PageObjects.confirmPage import confirmpage
from PageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class Testone(BaseClass):

    def test_e2e(self):
        log =self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage= homepage.shopItems()
        cards = checkoutpage.getcardtites(self)
        log.info("getting all the ")
        i = -1
        for card in cards:
            i = i + 1
            cardtext = card.text
            print(cardtext)
            if cardtext == "blackberry":
                checkoutpage.getcardfooter()[i].click()
        checkoutpage.clickcheckout(self)
        confirmpage.SendKeys(self).send_keys('ind')
        self.verifyLinkpresence("India")
        confirmpage.TextMessage(self).click()
        confirmpage.clickcheckbox(self).click()
        confirmpage.clickconfirm(self).click()
        confirmpage.checkfinalmessage(self).text

