#!/usr/bin/env python3
import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

nbi_name = sys.argv[1]
nbi_pwd = sys.argv[2]
host = sys.argv[3]
port = sys.argv[4]

POST_TOKEN_URL = "/controller/v2/tokens"
GET_SITES_URL = "/restconf/v1/data/ietf-alarms:alarms/alarm-list?limit=2000&is-cleared=false"

post_token_url = "https://" + host + ":" + port + POST_TOKEN_URL
headers_post = {'Content-Type': 'application/json', 'Accept': 'application/json'}

r = requests.post(post_token_url, headers=headers_post, json={"userName": nbi_name, "password": nbi_pwd}, verify=False)

token_id = r.json()['data']['token_id']
get_sites_url = "https://" + host + ":" + port + GET_SITES_URL
headers_get = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-ACCESS-TOKEN':token_id}

r = requests.get(get_sites_url, headers=headers_get, verify=False)
print(r.text)
