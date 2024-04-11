# accessing tuple elements
# access individual elements - indexes []
numbers = (1,2,3,4,5,[6,7,8],(9,10,11))

# accessing nested elements in a tuple
numbers = (1,2,3,4,5,[6,7,8],(9,10,11))
#print(numbers[5][0])

# access last element in a tuple using the negative index
numbers = (1,2,3,4,5,[6,7,8],(9,10,11))
#print(numbers[-1][-1]) 

# index slicing
numbers = (1,2,3,4,5,[6,7,8],(9,10,11))
#print(numbers[0:4])   # returns (1, 2, 3, 4)
print(numbers[:])   # returns (1, 2, 3, 4, 5, [6, 7, 8], (9, 10, 11))