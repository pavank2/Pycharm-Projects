import json
import requests
import pytest
from config.configurations import *
from config.resources import *
from jsonfiles import *




config = configparser.ConfigParser()
config.read('../config/properties.ini')
url = config['API']['endpoint']+APIRequests.postRequest
headers = {'Content-Type': 'application/json'}

#with open("postdata.json") as f:
 #   post_data = f.read()

#json_data = json.dumps(post_data)
response = requests.post(url, json=getjsonpayload(), headers=headers, )

res_json = response.json()

print(res_json['ID'])
assert response.status_code == 200


