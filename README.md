# pokemontcg_visualizer

***March 14th, 2021***
*Requires matplotlib and requests to be installed
Apps/Programs now Available!

*Takes ~5min to run!*
1) Data Retrieval 1.0 (count_each_mon.py) Uses pokemontcg API to return how many times each pokemon has appeared on a card and writes the dictionary to a file, but requires a list of each pokemon name to be provided
            -relies on pokenames.txt and get_counts.py

*INCOMPLETE - only works for some ranges, not 1-893*
2) Data Retrieval 2.0 (get_name_count.py) Uses pokemontcg API to return both Pokemon name and Appearances and writes the dictionary to a file. Does not require any modules or txt files as pokedex numbers simply range from 1-893, but several Pokemon come back with incorrect pseudonyms like "Zarude V" or "Blaine's Charizard".

3) Single Retrieval (input_and_response.py) With the aim to include all this on a website, I wanted user's to be able to quickly search their favorite Pokemon individually and receieve an immediate response instead of having to wait 5+min like in the two above examples. 
            -relies on get_counts.py to connect and query API

4) Graphing! (graphing.py) The initial end goal of this project for me was to create graphs for how many times Pokemon from each Generation appered on cards. This achieves this, but is not as pretty, or functional, as I would like it to be. Going forward my two goals are to improve on the graphs and host all of this on a website!

***February 26th, 2021***
The last project I worked on returned how many times each Pokemon appeared in the TCG using JSON files downloaded from https://github.com/PokemonTCG. In this project I hope to return more accurate/up-to-date data that I will then also visualize. 
Step 1 - Obtain a dictionary of all Pokemon occurences {Pokemon: Occurences}
Step 2 - Graph the data based on Generations. 