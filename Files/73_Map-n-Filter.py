
# Map and Filter in Python
# Both functions take in two parameters

# filter - takes in two parameters
# thus the function(lambda function) and the variable(list)
# num = [1,2,3,4,5,6,7,8,9,10]
# even = lambda x: (x % 2 == 0)
#
# results = list(filter(even,num))
# print(results)

# shorthand
num = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: (x % 2 == 0),num))
print(even)


# map - takes in two params
# thus the function(lambda) and the variable(list)
# numbers = [1,2,3,4,5,6,7,8,9,10]
# squared_numbers = lambda x: (x ** 2)

# res = list(map(squared_numbers,numbers))
# print(res)

#shorthand
numbers = [1,2,3,4,5,6,7,8,9,10]
squared_numbers = list(map(lambda x: (x ** 2),numbers))
print(squared_numbers)
