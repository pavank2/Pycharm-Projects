import pytest
import source.service as service
import unittest.mock as mock


@mock.patch("source.service.get_user_from_db")  # Tell what you are mocking
def test_get_user_from_db(mock_get_user_from_db):
     mock_get_user_from_db.return_value = "Mocked Alice" # Mock the return value

     user_name = service.get_user_from_db(1)   # Call the function which was mocked

     assert user_name == "Mocked Alice"        # Assert if mocked value is returned

@mock.patch("requests.get")
def test_get_users(mock_get):
     mock_response = mock.Mock()
     mock_response.status_code = 200
     mock_response.json.return_value = {"id": 1, "name": "John Doe"}
     mock_get.return_value = mock_response
     users = service.get_users()

     assert users == {"id": 1, "name": "John Doe"}