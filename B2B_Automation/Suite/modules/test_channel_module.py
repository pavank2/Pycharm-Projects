import requests
import jsonpath
import json


def test_create_inbound_channel(cookies, csrfheaders, channelurl, IBchanneldata):
    createIBChannelRes = requests.post(url=channelurl, data=json.dumps(IBchanneldata), cookies=cookies,
                                       headers=csrfheaders)
    assert createIBChannelRes.status_code == 201
    channel_id = createIBChannelRes.json()['id']
    print("IBChannelID=" + str(channel_id))
    print("\n")
    return channel_id


def test_create_outbound_channel(cookies, csrfheaders, channelurl, OBchanneldata):
    createOBChannelRes = requests.post(url=channelurl, data=json.dumps(OBchanneldata), cookies=cookies,
                                       headers=csrfheaders)
    assert createOBChannelRes.status_code == 201
    channel_id = createOBChannelRes.json()['id']
    print("OBChannelID=" + str(channel_id))
    print("\n")
    return channel_id


def test_get_inbound_channel(cookies, csrfheaders, channelurl, IBChannelID):
    getUrl = channelurl + "/" + IBChannelID
    getIBChannelResp = requests.get(url=getUrl, cookies=cookies, headers=csrfheaders)
    print(getIBChannelResp.content)
    print("\n")


def test_get_OB_channel(cookies, csrfheaders, channelurl, OBChannelID):
    getUrl = channelurl + "/" + OBChannelID
    getOBChannelResp = requests.get(url=getUrl, cookies=cookies, headers=csrfheaders)
    print(getOBChannelResp.content)
    print("\n")
