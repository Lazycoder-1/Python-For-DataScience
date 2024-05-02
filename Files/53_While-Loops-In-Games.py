# while loops in games 

play = True
while play == True:
    computer_guess = 10
    user_guess = int(input('Enter a number: '))
    if user_guess == computer_guess:
        play = False

print('Try again')

