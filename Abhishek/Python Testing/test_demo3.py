import pytest

@pytest.mark.usefixtures("firstprogram")
class Testexample:
    def test_Secondprogram(self):
        print(" i am the actual test case")

    def test_Secondprogram2(self):
        print(" i am the actual 2test case")

    def test_Secondprogram3(self):
        print(" i am the actual 3test case")

    def test_Secondprogram4(self):
        print(" i am the actual 4test case")
