from behave import *
from behave.formatter import json
import json

from Suite.modules.test_login_module import test_login_and_generate_tokens
from Suite.modules.test_rules_module import test_create_rule

use_step_matcher("re")

data_file = 'Suite/Data/login_data.json'
with open(data_file) as f:
    file_data = f.read()
data = json.loads(file_data)


url = data['URL']
rulesUrl = data['rulesUrl']
rulesData = data['rulesdata']


@then("Create processing rule")
def step_Create_rule(self):
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    test_create_rule(cookies, csrfheaders, rulesUrl, rulesData)
