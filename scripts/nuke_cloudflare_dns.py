import requests
import json
from pprint import pprint
from sys import argv

EMAIL = argv[1]
KEY = argv[2]
DNS = argv[3]
headers = {
	"X-Auth-Email" : EMAIL,
	"X-Auth-Key" : KEY,
	"Content-Type" : "application/json"
}

g = requests.get('https://api.cloudflare.com/client/v4/zones', headers = headers)
r = g.json()['result']

for i in r:
	if str(i['name']) in DNS:
		g = requests.get('https://api.cloudflare.com/client/v4/zones/%s/dns_records?per_page=500' % i['id'], headers = headers)
		d = g.json()
		if len(d['result']) > 0:
			for x in d['result']:
				n = requests.delete('https://api.cloudflare.com/client/v4/zones/%s/dns_records/%s' % (i['id'], x['id']), headers = headers)
				pprint(n.json())