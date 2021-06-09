import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.homePage import HomePage
from Testdata.Homepagedata import HomePagedata
from utilities.BaseClass import BaseClass


class Testhomepage(BaseClass):

    def test_formsubmittion(self, getdata):
        log =self.getLogger()
        homepage = HomePage(self.driver)
        log.info("firstname is"+ getdata["firstname"])
        homepage.getname().send_keys(getdata["firstname"])
        log.info("Email is" + getdata["email"])
        homepage.getemail().send_keys(getdata["email"])
        homepage.getpassword().send_keys(getdata["password"])
        homepage.gettickbox()
        log.info("geneder is" + getdata["gender"])
        self.selectoptionbytext(homepage.getgender(), getdata["gender"])
        homepage.getfinalsubmitbutton()
        Alerttext = homepage.getsubmitmesssage()
        assert ("Success! The Form" in Alerttext)
        self.driver.refresh()

    @pytest.fixture(params=HomePagedata.test_Homepage_data)
    def getdata(self, request):
        return request.param
