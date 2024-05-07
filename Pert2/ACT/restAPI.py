import requests

r = requests.get('http://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print('Status: ', r.status_code)