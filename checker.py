import requests
import hashlib
import sys


def request_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    print(response)
    if response.status_code != 200:
        return (f'Error: {response.status_code}')
    else:
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


def read_pass_from_file(filename):
    try:
        with open(filename, 'r') as file:
            password_list = file.readlines()
            for password in password_list:
                password = password.rstrip()
                count = check_if_pwned_password(password)
                if count:
                    with open('results.txt', 'a') as res_file:
                        result = (f'{password} was found {count} times!')
                        res_file.write(result)
                        res_file.write('\n')
                else:
                    with open('results.txt', 'a') as res_file:
                        result = (f'{password} was not found')
                        res_file.write(result)
                        res_file.write('\n')
    except IOError:
        file = open(filename, 'w')
        file.close()
        print('File not found, creating one')
    return 0


def main(args):
    if len(args) < 2:
        print('No args passed, checking for file')
        read_pass_from_file('pass_to_check.txt')

    else:
        for password in args:
            count = check_if_pwned_password(password)
            if count:
                print(f'{password} was found {count} times!')
            else:
                print(f'{password} was not found')
    return 'Done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
