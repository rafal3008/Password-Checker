import sys
from utility import *

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
