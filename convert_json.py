import collections
import json

mon = 0

for num in range (1, 9):
    with open('txt_files/Gen'+str(num)+'.json') as f: 
            data_dict = json.loads(f.read())
            mons = sum(data_dict.values())
            print(mons)
            mon += mons
            print(mon)


with open('txt_files/API Occurences.json') as g:
    straight = json.loads(g.read())
    reverse = collections.OrderedDict(list(straight.items())[::-1])

with open('txt_files/API Reverse.txt', 'w') as outfile:
    json.dump(reverse, outfile, indent=4)
