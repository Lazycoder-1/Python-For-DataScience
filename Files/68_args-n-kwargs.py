
# args and kwargs
# mostly used when you dont know the number of arguments or parameters for a function
# def gamers(*names):
#     for name in names:
#         print('Hi there ' + name)
# print(gamers('Kai','KSI','Tobi','Speed','Nick'))

# for arithmetics
# *nums = infinite number of parameters
# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(add(3,4,5,6,7))

# using kwargs = keyword arguments
def personal_info(**info):
    print(type(info))
    for key, value in info.items():
        print('This {} has a {}'.format(key,value))

print(personal_info(first_name='Kyle',last_name='Cooper',age=24,hobby='games'))

