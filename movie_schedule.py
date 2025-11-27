current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:30pm',
    'Frosty the Snowman': '3:45pm',
    'Christmas Vacation': '6:00pm'
}

print("Current movies playing:")
for key in current_movies:
    print(key)

movie = input("Which movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Sorry, we are not showing that movie.")
else:
    print("The showtime for " + movie + " is " + showtime + ".")