# pokemontcg_visualizer


***March 14th, 2021***
I have a number of apps/programs now (data retrieval, data organization, data visualization, game) that I either want to tie into a main file to be called from.
Or to incorporate them into the Django learning logs website I'm learning/creating. 
*Game   - rpsGame.py - is a Rock, Paper, Scissors game that I have modified to be bulbasaur, charmander, squirtle where fire beats grass, grass beats water and water beats fire. 
*Data Retieval
        -count_each_mon.py - Uses pokemontcg API to return how many times each pokemon has appeared **using a list of each pokemon that I provide
            -pokenames.txt

***February 26th, 2021***
The last project I worked on returned how many times each Pokemon appeared in the TCG using JSON files downloaded from https://github.com/PokemonTCG. In this project I hope to return more accurate/up-to-date data that I will then also visualize. 
Step 1 - Obtain a dictionary of all Pokemon occurences {Pokemon: Occurences}
Step 2 - Graph the data based on Generations. 