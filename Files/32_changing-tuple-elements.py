# changing tuple elements - once it is a nested list
numbers = (1,2,3,4,5,[6,7,8],(9,10,11))
#numbers[2] = 25   # this does not work since it imutable

# changing elements in a nested tuple
#numbers[5][1] = 25

# appending elements to nested tuples
numbers[5].append(100)

# tuple concatenation
items = (1,2,3,4,5)
new_items = items + (34,56,67)

print(new_items)