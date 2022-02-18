from behave import *
from behave.formatter import json
import json

from Suite.modules.test_login_module import test_login_and_generate_tokens
from Suite.modules.test_user_module import test_create_user

use_step_matcher("re")

data_file = 'Suite/Data/login_data.json'
with open(data_file) as f:
    file_data = f.read()
data = json.loads(file_data)


url = data['URL']
userurl = data['userurl']
userdata = data['userdata']


@then("Create a user")
def step_create_user(self):
    cookies, csrfheaders = test_login_and_generate_tokens(url)
    userid = test_create_user(cookies, csrfheaders, userurl, userdata)
