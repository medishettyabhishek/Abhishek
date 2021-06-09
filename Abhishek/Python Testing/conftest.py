import pytest


@pytest.fixture(scope="class")
def firstprogram():
    print("i will be printed first ")
    yield
    print("byeeeeeeee")

@pytest.fixture()
def loaddata():
    print("user profile data is being created ")
    return ["Abhishek", "shetty", "abhishekmedishetty@gmai.com"]

@pytest.fixture(params=["chrome", "IE","Firefox"])
def crossbrowser(request):
    return request.param



