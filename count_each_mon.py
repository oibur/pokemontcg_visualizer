#Runs each Pokemon name in pokenames.txt through the get_count function in get_counts.py
#Which retrieves how many times each of those pokemon have appeared on a card from an API
#Those PokemonName:Appearance pairs are then sorted into a dictionary and written to a JSON file
import json

from get_counts import get_count as gc

#Supply a list with the names of every Pokemon
with open('pokenames.txt', 'r') as f:
    dex_names = [line.strip() for line in f]

#Initialize dictionary
pokemon_counts = dict()

#Run get_count on each Pokemon in the list
#Append each name/get_count result to the dictionary in the process
for name in dex_names:
    try:
        pokemon_counts[name.title()] = gc(name)
    except KeyError:
        pass

#Create a sorted copy of the dictionary using functional python
occurences = dict(sorted(pokemon_counts.items(), key=lambda item: item[1]))

#Write the new sorted dictionary to a JSON file
with open('API Occurences.txt', 'w') as outfile:
    json.dump(occurences, outfile, indent=4)