# using the return method/function
# the return keyword converts it to it's correct data type

# def rookie():
#     '''The best drama series ever made'''
#     message = "Tim and Lucy"
#     return message
# rookie().upper()

# this function return sqaure numbers
# def double(num):
#     return num ** 2
# print(double(8))

# def my_function(x):
#   return 5 * x
# print(my_function(3))

def play_game(answer):
    if answer == 'yes':
        return True
    else:
        return False

#print(play_game('yes'))

#another scenario
if play_game('yes') == True:
    print('Good choice, let us continue the game')
else:
    print('See you next time, bye')






