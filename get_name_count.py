import json
import requests
#returns both count AND name from API based on #. 
#many pokemon are coming back with gym trainer names 
#keep getting "IndexError: list index out of range" when running all 893

api_key = 'c2eaa76b-c34c-4d3a-8f33-da95a230d9ea'
api_base_url = 'https://api.pokemontcg.io/v2'

name_counts = dict()

def get_name_count(num):
    endpoint_path = f'/cards?q=nationalPokedexNumbers:{num}'
    endpoint = f'{api_base_url}{endpoint_path}'
    data = (requests.get(endpoint, data={'X-api-key': api_key})).json()
    api_data = data['data']
    name_source = api_data[0]
    names = name_source['name']
    count = data['count']
    name_counts[names] = count

for num in range (1,152):
    get_name_count(num)

with open('Gen1.txt', 'w') as outfile:
    json.dump(name_counts, outfile, indent=4)