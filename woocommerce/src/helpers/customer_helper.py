from src.utilities.genericUtilities import generate_random_email_passwd
from src.utilities.requestsUtility import RequestsUtility
class CustomerHelper(object):

    def __init__(self):
        self.req = RequestsUtility()

    def create_customer(self,email=None,password=None,**kwargs):


        if not email:
            ep = generate_random_email_passwd()
            email = ep['email']
        if not password:
             password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        create_user_json = self.req.post('customers',payload=payload,expected_status_code=201)

        return create_user_json




