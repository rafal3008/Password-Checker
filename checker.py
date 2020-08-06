import requests
import hashlib


def request_api_data(query_char):
    # request data from server
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # need to be a hash
    response = requests.get(url)
    return response


def check_if_pwned_password(password):
    # need to encode password, and then hash it
    hash_password = (hashlib.sha1(password.encode('utf-8')).hexdigest())
    hash_password = hash_password.upper()
    print(hash_password)


check_if_pwned_password('password')
