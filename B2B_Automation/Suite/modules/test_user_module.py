import requests
import jsonpath
import json


def test_create_user(cookies, csrfheaders, userurl, userdata):
    createUserChannel = requests.post(url=userurl, data=json.dumps(userdata), cookies=cookies,
                                      headers=csrfheaders)
    user_id = createUserChannel.json()['id']
    print("UserID=" + str(user_id))
    print("\n")
    return user_id
