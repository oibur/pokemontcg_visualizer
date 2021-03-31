# pokemontcg_visualizer
***March 31st, 2021***
Hello fellow Code Louisville member and welcome to my project, hope you like Pokemon! :)
The only libraries required for this project are requests, and matplotlib. 
The only special instructions, listed below, are things you can do to reduce waiting times by reduced querying. 

My project can do a few fun things! 
1) If you run input_and_response.py, you will be asked to name a Pokemon (Examples of Pokemon names include: Raichu, Mewtwo, Steelix and Cufant.) and the program will connect to an API and return how many times that Pokemon has appeared on a unique card over the past 25 years.
2) Retrieval 1.0: If you run count_each_mon.py it will connect to an API and return how many times EVERY Pokemon has appeared, as a dictionary, written to a txt file named API Occurences. --- This includes 893 api connections and takes roughly 5 min to run on my computer, feel free to shorten the items in pokemon.txt, in the txt_files folder, to shorten this retrieval time.
3) Retrieval 2.0: If you run get_name_count.py it does the same as above, but without requiring a txt file to run (it also retrieves the Pokemons name for me). This time written to a txt file named API Occurences 2 --- Again this takes roughly 5 min to run, to shorten the time here, you may decrease the range from 1:894 to say...1:26 (that way you still include the mascot Pikachu!)
4) pie_chart.py, small_graphs.py and bar_graphs.py all create visuals of the data that I obtained to be displayed on the Django page I developed and have hosted on Heroku at: dadairai-pokemon.herokuapp.com.
5) Going forward my next goals for this project after this class are to get my input_and_response.py program to be included on my site, and to get the image.py program to work in a way to display picturs on my site.

The 3+ project requirements I fulfilled include:
-Create a dictionary, or list, populate it with several values, retrieve at least one value, and use it in your program.
-Read data from an external file, such as text, JSON, CSV, etc and use that data in your application.
-Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
-Connect to an external/3rd party API and read data into your app.
-Visualize data in a graph, chart, or other visual representation of data.
-Use pandas, matplotlib, and/or numpy to perform a data analysis project. 

If you care to take a look this projects 'Journal' is also available below. Thank you for visiting today, have a great week!











***March 25th, 2021***
I was able to break down the data in additional ways, make more graphs and have those graphs look a BIT prettier. More importantly I was able to figure out enough Django to get this all HOSTED!!! at http://dadairai-pokemon.herokuapp.com/. However the comment section has broken between hosting it local virtaully vs public on Heroku now.


***March 14th, 2021***
*Requires matplotlib and requests to be installed
Apps/Programs Available!

*Takes ~5min to run!*
1) Data Retrieval 1.0 (count_each_mon.py) Uses pokemontcg API to return how many times each pokemon has appeared on a card and writes the dictionary to a file, but requires a list of each pokemon name to be provided
            -relies on pokenames.txt and get_counts.py

*INCOMPLETE - only works for some ranges, not 1-893*
2) Data Retrieval 2.0 (get_name_count.py) Uses pokemontcg API to return both Pokemon name AND Appearances, then writes the dictionary to a file. Does not require any modules or txt files, but several Pokemon come back with incorrect pseudonyms like "Zarude 'V'" or "'Blaine's' Charizard".

3) Single Retrieval (input_and_response.py) With the aim to include all this on a website, I wanted user's to be able to quickly search their favorite Pokemon individually and receieve an immediate response instead of having to wait 5+min like in the two above examples. 
            -relies on get_counts.py to connect and query API

4) Graphing! (graphing.py) The initial end goal of this project for me was to create graphs for how many times Pokemon from each Generation appered on cards. This achieves this, but is not as pretty, or functional, as I would like it to be. Going forward my two goals are to improve on the graphs and host all of this on a website!

***February 26th, 2021***
I just finished this project: https://github.com/oibur/bryans_pokemontcg_counter that returned how many times each Pokemon appeared in the TCG using JSON files downloaded from https://github.com/PokemonTCG. In this project I hope to, at any point down the road, return accurate/up-to-date data and perhaps visualize it as well.
Step 1 - Obtain a dictionary of all Pokemon occurences {Pokemon: Occurences}
Step 2 - Graph the data based on Generations. 