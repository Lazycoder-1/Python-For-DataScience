# other useful lists methods
letters = ['a','b','c','d','e','f','g','h','i','j']

# the length of a list
#print(len(letters)) 

# other scenario
li = ['a','b','c','d',['e','f','g'],'h','i',['j']]
#print(li)

#using the range method
#print(list(range(12)))

# using the zip method, it combines two list e.g.
# expected results [('Bradford', 34), ('Chen', 29), ('Grey', 47), ('Diaz', 31),
# ('Harper', 33), ('Aaron', 26)]

names = ['Bradford','Chen','Grey','Diaz','Harper','Aaron']
ages = [34,29,47,31,33,26]

combined_list = list(zip(names,ages))
print(combined_list)

# using the count method , the number of times a number appears in a list
numbers = [1,1,1,2,3,4,6,7,6,8,9,8,5,3,4,6,78,5,4,68,8,8,78,65,4,43,6]
print(numbers.count(6))
