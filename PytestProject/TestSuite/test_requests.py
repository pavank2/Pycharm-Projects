import requests
import pytest

@pytest.fixture(scope="module")  #scope is entire module. Calls only once
def my_setup():
    print("Testing fixtures")
    return {'id':20, 'name':'Pavan'}

@pytest.mark.smoke
def test_get(my_setup):
    get_response = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "John Doe"}, )

    print("Test passed")
    #import pdb; pdb.set_trace()


def test_post():
    post_response = requests.post("http://216.10.245.166/Library/Addbook.php", json={

        "name": "Learn Appium Automation with Java",
        "isbn": "bcdzsc",
        "aisle": "227",
        "author": "John foe"
    }, headers={"Content-Type":"Application/json"},)

    assert post_response.status_code == 200,\
    f'Expected status code is 200 but actual is {post_response.status_code}'
