import requests
import hashlib


def request_api_data(query_char):
    # request data from server
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    return response


def get_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for item, count in hashes:
        if item == hash_to_check:
            return count
    return 0


def check_if_pwned_password(password):
    hash_password = (hashlib.sha1(password.encode('utf-8')).hexdigest())
    hash_password = hash_password.upper()
    first_five = hash_password[:5]
    tail = hash_password[5:]
    print(first_five, tail)
    response = request_api_data(first_five)

    return get_leaks_count(response, tail)


check_if_pwned_password('password')
