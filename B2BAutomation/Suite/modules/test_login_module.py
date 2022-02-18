import requests
import jsonpath
import json

from requests.structures import CaseInsensitiveDict

data_file = 'Suite/Data/login_data.json'

with open(data_file) as f:
    file_data = f.read()

data = json.loads(file_data)
headers = data['headers']


def test_login_and_generate_tokens(url):
    # Login
    v_response = requests.get(url=url, headers=headers, allow_redirects=False)
     print(v_response.status_code)
     print("\n")
    # print(v_response.cookies)
    # print("\n")
     print(v_response.headers["Location"])
    # print("\n")
    v_response1 = requests.get(url=v_response.headers["Location"], headers=headers,
                               allow_redirects=False)
    contentBody = v_response1.content.__str__()
    url = (contentBody[contentBody.find("action=") + 8:contentBody.find("action=") + 246])
    sessionCode = (url[url.find("session_code=") + 13:url.find("session_code=") + 56])
    executionCode = (url[url.find("execution=") + 10:url.find("execution=") + 46])
    tabID = (url[url.find("tab_id=") + 7:url.find("tab_id=") + 18])
    # print(v_response1.cookies)
    # print("\n")
    # print(url)
    # print("\n")
    # print(sessionCode)
    # print("\n")
    # print(executionCode)
    # print("\n")
    # print(tabID)

    # Redirect
    logindata = data['loginData']
    redUrl = data['redurl']
    redirectUrl = redUrl.format(sessionCode, executionCode, tabID)
    # print(redirectUrl)
    res1 = requests.post(url=redirectUrl, data=logindata, cookies=v_response1.cookies, allow_redirects=False)
    # print(res1.headers["location"])
    # print("\n")
    res2 = requests.get(url=res1.headers["location"], headers=headers, cookies=v_response.cookies,
                        allow_redirects=False)
    # print(res2.headers["Location"])
    # print("\n")
    res3 = requests.get(url=res2.headers["Location"], headers=headers, cookies=v_response.cookies,
                        allow_redirects=False)

    # csrf
    csrfUrl = data['csrfurl']
    csrf = requests.get(url=csrfUrl, headers=headers, cookies=v_response.cookies, allow_redirects=False)
    assert csrf.status_code == 200
    csrf_token = json.loads(csrf.content)['csrfToken']
    # print(csrf_token)
    # print("\n")
    headers["X-CSRF-TOKEN"] = csrf_token
    print("Generated Header=" + str(headers))
    print("\n")
    print(v_response.cookies)
    print("\n")

    return v_response.cookies, headers
