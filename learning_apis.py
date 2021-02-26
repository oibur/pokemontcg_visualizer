import json

from get_counts import get_count as gc

with open('pokenames.txt', 'r') as f:
    dex_names = [line.strip() for line in f]

pokemon_counts = dict()

for name in dex_names:
    try:
        pokemon_counts[name.title()] = gc(name)
    except KeyError:
        pass

with open('API Occurences.txt', 'w') as outfile:
    json.dump(pokemon_counts, outfile, indent=4)