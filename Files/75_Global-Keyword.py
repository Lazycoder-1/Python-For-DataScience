# access variables within functions
# thus using the global keyword

# this code block will not update x in the defined function
# x = 100
# def func(x):
#     x = 200
#     print('X was {}'.format(x))
#
#     x = 300
#     print('X is now {}'.format(x))
#
# print(x)

# to access a variable(y) in a function , we use the global keyword
y = 100

def func():
    global y
    print('Y was {}'.format(y))

    y = 200
    print('Y is now {}'.format(y))

print(y)
func()
print(y)


