import json

#uses text file and module to return dict of names and counts. Only counts are from API

from get_counts import get_count as gc

with open('pokenames.txt', 'r') as f:
    dex_names = [line.strip() for line in f]

pokemon_counts = dict()

for name in dex_names:
    try:
        pokemon_counts[name.title()] = gc(name)
    except KeyError:
        pass

occurences = dict(sorted(pokemon_counts.items(), key=lambda item: item[1]))

with open('API Occurences.txt', 'w') as outfile:
    json.dump(occurences, outfile, indent=4)