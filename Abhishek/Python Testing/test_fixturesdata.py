
import pytest
import baseclass

@pytest.mark.usefixtures("loaddata")
class Testexample2(baseclass):

    def test_editprofile(self, loaddata):
       log =   self.getlogger()
        #print(loaddata)
