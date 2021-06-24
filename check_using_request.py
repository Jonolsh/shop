

import requests

response = requests.get('http://127.0.0.1:8000/cart/test_session/')

print(response)

print(response.status_code)


print('*'*10)
print(response.headers)

# print(response.headers['Set-cookie'])

print(response.text)

print(response.content)


