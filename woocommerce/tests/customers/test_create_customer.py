import pytest
import logging as logger
import requests

from src.utilities.genericUtilities import generate_random_email_passwd
from src.helpers.customer_helper import CustomerHelper
from src.dao.customers_dao import CustomersDAO


def test_create_customer():
    logger.info('New customer create')
    rand_info = generate_random_email_passwd()
   # print(rand_info)
    email=rand_info['email']
    password=rand_info['password']

    #create payload

   # payload = {'email': email, 'password':password}
    #make call

    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email,password=password)

    #verify status code of call

    #verify email in response
    assert cust_api_info['email'] == email
    assert cust_api_info['first_name'] == ''


    #verify customer is created in DB

    cust_dao = CustomersDAO()

    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db,\
    f'{id_in_api}Not same as {id_in_db}'

@pytest.mark.tcid01
def test_mock_api():
    rs_json= requests.get('https://d5bce197-be3c-438e-bf43-1a798b8e9477.mock.pstmn.io/books',headers={},params={})

    print(rs_json.json())
    print(rs_json.headers)