import http.client
import json
token = '6b29ad3dc7c94db7b0c2c4b5b8a05980'

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': token, 'X-Response-Control': 'minified' }
connection.request('GET', '/v1/competitions', None, headers )
response = json.loads(connection.getresponse().read().decode())

for i in response:
    print(i)