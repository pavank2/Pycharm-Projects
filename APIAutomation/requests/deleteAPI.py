import requests
import configparser

import sys

sys.path.insert(0, "C:\\Users\\PK\\PycharmProjects\\APIAutomation\\config")

from configurations import *
from jsonfiles import *
from resources import *

config = configparser.ConfigParser()
config.read('../config/properties.ini')
url = config['API']['endpoint']+APIRequests.postRequest
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=getjsonpayload("zcfsdcsa"), headers=headers, )

res_json = response.json()


bookId = res_json['ID']


response_del = requests.post("http://216.10.245.166/Library/DeleteBook.php",json={
       "ID":bookId
     },headers={"Content-Type":"Application/json"},)

assert response_del.status_code == 200
print(response_del.json())

#Authentication code

