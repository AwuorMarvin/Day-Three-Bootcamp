import requests
from pprint import pprint
request = requests.get('https://api.github.com/events')

try:
	response = request.text
	pprint (response)
except requests.exceptions.RequestException as e:
    print(e)