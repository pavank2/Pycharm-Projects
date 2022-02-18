from behave import *
from behave.formatter import json
import json
import jsonpath
from Suite.modules.test_login_module import test_login_and_generate_tokens
from Suite.modules.test_partner_module import test_create_sender, test_create_receiver, test_delete_partner

use_step_matcher("re")

data_file = 'Suite/Data/login_data.json'
with open(data_file) as f:
    file_data = f.read()
data = json.loads(file_data)


url = data['URL']
senderpartnerdata = data['senderPartnerdata']
partnerurl = data['partnerUrl']
receiverpartnerdata = data['recieverPartnerdata']
delPartnerUrl = data['deletePartnerUrl']


@then("Create Sender Partner")
def step_Create_Sender(self):
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    SenderId = test_create_sender(cookies, csrfheaders, partnerurl, senderpartnerdata)


@then("Create Receiver partner")
def step_Create_Receiver(self):
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    receiverid = test_create_receiver(cookies, csrfheaders, partnerurl, receiverpartnerdata)


@then("Delete Partner")
def step_Delete_Partner(partnerId):
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    test_delete_partner(cookies, csrfheaders, delPartnerUrl, partnerId)
