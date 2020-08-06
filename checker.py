import requests
import hashlib
import sys


def request_api_data(query_char):
    # what if bad response
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
    hash_password = (hashlib.sha1(
        password.encode('utf-8')).hexdigest()).upper()
    first_five = hash_password[:5]
    tail = hash_password[5:]
    response = request_api_data(first_five)

    return get_leaks_count(response, tail)


def main(args):
    # what if there arent any arguments passed
    for password in args:
        count = check_if_pwned_password(password)
        if count:
            print(f'{password} was found {count} times!')
        else:
            print(f'{password} was not found')
    return 1


main(sys.argv[1:])
