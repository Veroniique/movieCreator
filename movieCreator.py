'''
This project is intended to store a list of movies/series you enter.
You can remove movies/series at any time.
You can also ask it to randomize a movie/series from your list
'''

'''
Project goals:
- remove all duplicates automatically
- set capitalization to allow all characters
- after user enters movies/series, shows a list off all
- button to view current list of series/movies side by side
- display outputs with 1 letter capatalized
'''

#Intro for user
print("Movie/Series simulator \n")
print("1: Enter the movies/series you plan to see. \n"
      "2: Remove ones you've already seen. \n"
      "3: Click the randomizer to get a random movie/series from your list to watch. \n")

#Prompts user for movie and adds to a list
movie_list = []

movie = input("What movie(s) do you want to add to the list? ")
print(f"{movie} has been added to the list.")
movie_list.append(movie)

#Prompts user for series and adds to a list
series_list = []

series = input("What series do you want to add to the list? ")
print(f"{series} has been added to the list.")
series_list.append(series)
