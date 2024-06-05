
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
def x():
    num = 20
    return num
print(num)
# This error NameError: name 'num' is not defined will occur because num is only function scope available.



