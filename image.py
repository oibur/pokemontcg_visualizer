#Retrieves how many times each pokemon has appeared on a card 
#from API as dictionary and writes dictionary to JSON file 
#Many pokemon are coming back with gym trainer names
#Keep getting "IndexError: list index out of range" when running all 893
import json
import requests

#Members of Code Louisville, please feel free to ask for my API
api_key = 'c2eaa76b-c34c-4d3a-8f33-da95a230d9ea'

#Initialize dictionary
name_counts = dict()

def get_name_count(num):
    #sets the API endpath based on the pokemons dex num
    endpoint = f'https://api.pokemontcg.io/v2/cards?q=nationalPokedexNumbers:{num}'
    data = (requests.get(endpoint, data={'X-api-key': api_key})).json()
    #Retrieves data from API and append to dictionary
    print(data['data'][0]['images']['small'])

get_name_count(26)