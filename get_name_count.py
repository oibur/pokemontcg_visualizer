#Retrieves how many times each pokemon has appeared on a card from API as dictionary
#Writes dictionary to JSON file -Many pokemon are coming back with gym trainer names
#Keep getting "IndexError: list index out of range" when running all 893
import json
import requests

#Members of Code Louisville, please feel free to ask for my API
api_key = '...'
api_base_url = 'https://api.pokemontcg.io/v2'

#Initialize dictionary
name_counts = dict()

def get_name_count(num):
    #sets the API endpath based on the pokemons dex num
    endpoint_path = f'/cards?q=nationalPokedexNumbers:{num}'
    endpoint = f'{api_base_url}{endpoint_path}'
    data = (requests.get(endpoint, data={'X-api-key': api_key})).json()
    #Retrieves name from API
    api_data = data['data']
    name_source = api_data[0]
    names = name_source['name']
    #Retrieves apperances from API
    count = data['count']
    #Appends data to dictionary
    name_counts[names] = count

#Input what range of pokemon dex numbers you want to retrieve
for num in range (1,26):
    get_name_count(num)

#Writes dictionary to JSON file
with open('API Occurences2.txt', 'w') as outfile:
    json.dump(name_counts, outfile, indent=4)