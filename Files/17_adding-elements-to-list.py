# adding items to lists
# four methods: += , append, extend, insert 

games = ['gta','pes','fifa','cod','nba']
fav = ['fifa','pes','cod','valorant']

# list concatenation 
# add single item to the list e.g
#print(games + ['valorant'])

# using the += operator
games += fav


# using the append() method
movies = ['the rookie','outer banks']
#movies.append('the mayor of kingstown')
#print(movies)

# nested list with the append method
unwatch = ['see','prison break','breaking bad']
#movies.append(unwatch)


# using the .extend method , this will create something like this
# ['the rookie', 'outer banks', 'see', 'prison break', 'breaking bad']
movies = ['the rookie','outer banks']
unwatch = ['see','prison break','breaking bad']
#movies.extend(unwatch)

# using the insert method
# this takes in two parameters, index position[1] and the element to be inserted
unwatch.insert(0, 'the rookie')
# e.g ['the rookie', 'see', 'prison break', 'breaking bad'] 
print(unwatch)