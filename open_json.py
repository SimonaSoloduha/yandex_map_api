import json
import urllib.request as urllib2

#Address for sending JSON requests
url = 'https://api.direct.yandex.ru/v4/json/'

#data for OAuth authorization
token = 'e4d3b4d2a7444fa384a18cda5cd1c8d9'

#Yandex.Direct login
login = 'agrom'

#input data structure (dictionary)
data = {
   'method': 'GetClientInfo',
   'token': token,
   'locale': 'ru',
   'param': [login]
}

jdata = json.dumps(data, ensure_ascii=False).encode('utf8')

#execute the request
response = urllib2.urlopen(url, jdata)

#output the result
print(response.read().decode('utf8'))
