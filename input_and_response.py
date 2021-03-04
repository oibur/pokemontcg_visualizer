from get_counts import get_count as gc
#asks user for a Pokemon and returns how many cards they have

pokemon = ""
try:
    while pokemon != 'quit':
        pokemon = input("Please enter the name of a Pokemon (or enter quit): ")
        number = gc(pokemon)
        if pokemon == 'quit':
            print("Gotta Catch Em' All!")
        elif number == 0:
            print(f'{pokemon} is not the name of a Pokemon!')
        else:
            print(f'{pokemon.title()} has appeared on {number} cards over the past 25 years!')
except KeyError:
    print("Two named Pokemon are tricky, try quotes around the names next time")