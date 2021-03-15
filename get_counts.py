#Given a Pokemon name get_count will run the name through an API 
#and return how many times that pokemon has appeared on a card
import requests

#Members of Code Louisville, please feel free to ask for my API
api_key = '...'
api_base_url = 'https://api.pokemontcg.io/v2'

def get_count(name_of_pokemon):
    endpoint_path = f'/cards?q=name:{name_of_pokemon}'
    endpoint = f'{api_base_url}{endpoint_path}'
    data = (requests.get(endpoint, data={'X-api-key': api_key})).json()
    counts = data['count']
    return counts
