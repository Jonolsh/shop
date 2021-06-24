import requests

import time


sessionid_var = None

with requests.Session() as session:
	# sessionid = session.cookies.get('SESSIONID')
	# print(sessionid)


	response = session.get('http://127.0.0.1:8000/cart/test_session/')
	print(response.headers)

	time.sleep(3) # Сон в 2 секунды
	print('*'*10)

	response = session.get('http://127.0.0.1:8000/cart/test_session/')
	print(response.headers)

	print(response.headers['Set-Cookie'])
	print(type(response.headers['Set-Cookie']))

	# print(session.cookies)
	# # <RequestsCookieJar[<Cookie sessionid=e2w032rbd53td6676tntzfmh8n2him26 for 127.0.0.1/>]>

	# # выведет sessionid
	# print(session.cookies['sessionid'])
	# # izy4o01edeisa43n7guraarln0cs97a4

	# sessionid_var = session.cookies['sessionid']

	# print(response.text)
	# # Вы уже отправили комментарий



# # в

# print('*'*10)
# # sessionid_var содержит id  сессии  (sessionid) полученный выше
# cookies = {'sessionid': sessionid_var}

# response = requests.get('http://127.0.0.1:8000/cart/test_session/', cookies=cookies)

# # выведет тот же самый sessionid, т.е. сесия работает через id
# print(response.headers['Set-Cookie'])
# # sessionid=5yjs7lqqcp8x4xezsf216ljj1pwgcp1r; expires=Wed, 27 Jan 2021 23:20:06 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax