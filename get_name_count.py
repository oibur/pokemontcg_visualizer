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
    name_counts[data['data'][0]['name']] = data['count']

######     Input what range of pokemon dex numbers you want to retrieve     ######
for num in range (1, 894):
    try:
        get_name_count(num)
    except IndexError:
        pass

#Writes dictionary to JSON file
with open('API Occurences2.txt', 'w') as outfile:
    json.dump(name_counts, outfile, indent=4)