import logging as logger
import random
import string

def generate_random_email_passwd(domain=None,email_prefix=None):
    logger.debug("Generating email and password")

    if not domain:
        domain = 'supersqa.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_string = ''.join(random.choices(string.ascii_lowercase,k=5))

    email = email_prefix+'_'+ random_string+'@'+domain

    password = ''.join(random.choices(string.ascii_letters,k=8))

    random_info = {'email': email, 'password': password}

    return random_info
