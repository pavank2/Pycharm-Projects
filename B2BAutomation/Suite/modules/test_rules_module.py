import requests
import jsonpath
import json


def test_create_rule(cookies, csrfheaders, rulesUrl, rulesData):
    ruleResponse = requests.post(url=rulesUrl, data=json.dumps(rulesData), cookies=cookies,
                                 headers=csrfheaders)
    print(ruleResponse.status_code)
    print("\n")
    print(ruleResponse.content)
    print("\n")
