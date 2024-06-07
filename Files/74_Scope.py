
# LEGB rule
# Local , Enclosing , Global and Built In.
# variables called in within a function are not global variables e.g num can not be called when not created first

# num = 35
# def func ():
#     num = 100
#     return num
# print(num)

# Local
# only accessible within function or lambda function   e.g below
# def x():
#     num = 20
#     return num
# print(num)
# This error NameError: name 'num' is not defined will occur because num is only function scope available.

# Enclosing = Non local scope
# def space():
#     word = 'Enclosing'
#
#     def nested_space():
#         word = 'Local'
#         print('Hello from '+ word)
#     nested_space()
#
# print(space())

# Global = the global variable
# it cannot be within a function where it is not defined...
word = 'Global'
def space():
    #word = 'Enclosing'

    def nested_space():
        #word = 'Local'
        print('Hello from '+ word)
    nested_space()

# Built In
# thus the built in functions
list()

print(space())