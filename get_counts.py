#Given a Pokemon name get_count will run the name through an API 
#and return how many times that pokemon has appeared on a card
import requests

#Members of Code Louisville, please feel free to ask for my API
api_key = 'c2eaa76b-c34c-4d3a-8f33-da95a230d9ea'

def get_count(name_of_pokemon):
    endpoint = f'https://api.pokemontcg.io/v2/cards?q=name:{name_of_pokemon}'
    data = (requests.get(endpoint, data={'X-api-key': api_key})).json() 
    return data['count']