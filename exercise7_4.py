movie_0 = {
    "name": "Casablanca",
    "year": 1942
}
movie_1 = {
    "name": "Forrest Gump",
    "year": 1994
}
movie_2 = {
    "name": "Avatar",
    "year": 2009
}
movie_3 = {
    "name": "Schindler's List",
    "year": 1993
}
movie_4 = {
    "name": "Wednesday",
    "year": 2022
}
movie_5 = {
    "name": "Hotel Mumbai",
    "year": 2018
}
movie_6 = {
    "name": "Home alone",
    "year": 1990
}

# creating a list which consists a lists of movies:
movies = [movie_0, movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

# creating two empty lists:
old_movies = []
new_movies = []

# for-loop goes through years of the movies and
# using condition statement creates new lists of movies:
for movie in movies:
    if movie["year"] >= 2000:
        new_movies.append(movie["name"])
    else:
        old_movies.append(movie["name"])


# use of join () function to pring a string of movies in one line:
new_movies_print = ", ".join(new_movies)
old_movies_print = ", ".join(old_movies)

# printing result:
print("These movies have been released in year 2000 or later:")
print(f"{new_movies_print}\n")
print("These movies have been released before the year 2000:")
print(old_movies_print)