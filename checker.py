import requests


def request_api_data(query_char):
    # request data from server
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # need to be a hash
    response = requests.get(url)
    print(response)  # if everything is good, should get <Response [200]>
    return response


request_api_data('CBDFA')
