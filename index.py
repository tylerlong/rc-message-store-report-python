from ringcentral_client import RestClient, PRODUCTION_SERVER

rc = RestClient("clientId", "clientSecret", PRODUCTION_SERVER)

rc.authorize('username', 'extension', 'password')

r = rc.get('/restapi/v1.0/account/000000/message-store-report/111111')
print(r.text)

r = rc.get('/restapi/v1.0/account/000000/message-store-report/111111/archive')
print(r.text)

r = rc.get('/restapi/v1.0/account/000000/message-store-report/111111/archive/0')
print(len(r.content))
file = open("test0.zip", "wb")
file.write(r.content)
file.close()

r = rc.get('/restapi/v1.0/account/000000/message-store-report/111111/archive/1')
print(len(r.content))
file = open("test1.zip", "wb")
file.write(r.content)
file.close()
