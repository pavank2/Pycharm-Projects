from behave import *
from behave.formatter import json
import requests
import jsonpath
import json
from Suite.modules.test_channel_module import test_create_inbound_channel, test_create_outbound_channel, \
    test_get_inbound_channel
from Suite.modules.test_login_module import test_login_and_generate_tokens

use_step_matcher("re")

data_file = 'Suite/Data/login_data.json'
with open(data_file) as f:
    file_data = f.read()
data = json.loads(file_data)

url = data['URL']
IBchanneldata = data['IBchanneldata']
channelurl = data['channelurl']
OBchanneldata = data['OBchanneldata']


@then("Create inbound channel")
def step_Create_Inbound_Channel(self):

    #prerequistes - file load
    #create the resource or call the API
    #verify results
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    inboundChannelID = test_create_inbound_channel(cookies, csrfheaders, channelurl, IBchanneldata)


@then("Create outbound channel")
def step_Create_Outbound_Channel(self):
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    outboundChannelID = test_create_outbound_channel(cookies, csrfheaders, channelurl, OBchanneldata)

