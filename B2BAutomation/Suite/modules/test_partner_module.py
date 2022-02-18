import requests
import jsonpath
import json


def test_create_sender(cookies, csrfheaders, partnerurl, senderpartnerdata):
    createSPartnerRes = requests.post(url=partnerurl, data=json.dumps(senderpartnerdata), cookies=cookies,
                                      headers=csrfheaders)
    assert createSPartnerRes.status_code == 201
    sender_partner_id = createSPartnerRes.json()['internalId']
    print("SenderID=" + str(sender_partner_id))
    print("\n")
    return sender_partner_id


def test_create_receiver(cookies, csrfheaders, partnerurl, receiverpartnerdata):
    createRPartnerRes = requests.post(url=partnerurl, data=json.dumps(receiverpartnerdata), cookies=cookies,
                                      headers=csrfheaders)
    assert createRPartnerRes.status_code == 201
    receiver_partner_id = createRPartnerRes.json()['internalId']
    print("ReceiverID=" + str(receiver_partner_id))
    print("\n")
    return receiver_partner_id


def test_delete_partner(cookies, csrfheaders, delPartnerUrl, partnerId):
    delurl = delPartnerUrl.format(partnerId)
    deletePartnerRes = requests.delete(url=delurl, cookies=cookies, headers=csrfheaders)
    assert deletePartnerRes.status_code == 204
    print(deletePartnerRes.status_code)
    print("\n")
