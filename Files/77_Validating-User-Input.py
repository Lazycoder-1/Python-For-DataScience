
# validating user input(s)

# user entering a different data format
# method that checks if a variable contains a digit isDigit()
# def request_age():
#     age = ''
#     while age.isdigit() == False:
#         age = input('Enter your age: ')
#         if age.isdigit() == False:
#             print('Please enter age in numbers')
#     return(int(age))
#
# print(request_age())

# user wants to play a game again or not
def play_game():
    answer = ''
    while answer.lower() not in ['y','n']:
        answer = input('Do you want to play again: ')
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print('Please enter Y for Yes or N for No')
    # return answer
print(play_game())















