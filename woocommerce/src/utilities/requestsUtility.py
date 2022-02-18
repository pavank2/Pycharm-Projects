import requests
import os
import json
from requests_oauthlib import OAuth1
from src.configs.hosts_config import API_HOSTS
from src.utilities.credentialsUtility import CredentialsUtility
class RequestsUtility(object):

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV','test')
        self.base_url = "http://192.168.0.101:8888/coolsite/wp-json/wc/v3/"  #to make it generic API_HOSTS[self.env]
       # self.auth = OAuth1("ck_6e6976bcfdf614c070d07b7993ed42bf3c09180c","cs_c8a69cbabd38a00f1b865bc60ee1ca788e53d157")
        self.auth = OAuth1(wc_creds['wc_key'],wc_creds['wc_secret'])


    def post(self,endpoint,payload=None,headers=None,expected_status_code=201):

        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.post(url=url,data=json.dumps(payload),headers=headers,auth=self.auth)
        import pdb; pdb.set_trace()
        self.status_code = rs_api.status_code\

        assert self.status_code == expected_status_code  , \
        f'Expected {expected_status_code} but got {self.status_code}'

      #  print(rs_api.json())
        return rs_api.json()


