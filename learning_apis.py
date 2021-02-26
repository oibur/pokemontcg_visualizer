import json
import requests
from pokemontcgsdk import Card

with open('testing.txt', 'r') as f:
    dex_names = [line.strip() for line in f]

occurences = dict()

api_key = 'c2eaa76b-c34c-4d3a-8f33-da95a230d9ea'
api_base_url = f'https://api.pokemontcg.io/v2'

for name in dex_names:
    try:
        endpoint_path = f'/cards?q=name:{name}'
        endpoint = f'{api_base_url}{endpoint_path}'
        data = (requests.get(endpoint, data={'X-api-key': api_key})).json()
        zacian = data['count']
        occurences[name] = zacian
    except KeyError:
        zacian = 0

with open('API Occurences.txt', 'w') as outfile:
    json.dump(occurences, outfile, indent=4)
