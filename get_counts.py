import requests

#returns card counts for each pokemon from API
#requires a txt file with the names of every pokemon

api_key = '...'
api_base_url = 'https://api.pokemontcg.io/v2'

def get_count(name_of_pokemon):
    endpoint_path = f'/cards?q=name:{name_of_pokemon}'
    endpoint = f'{api_base_url}{endpoint_path}'
    data = (requests.get(endpoint, data={'X-api-key': api_key})).json()
    counts = data['count']
    return counts
