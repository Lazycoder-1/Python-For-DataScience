
# create the five lives game using functions
import random

user_lives = 5

def five_lives(user_guess):
    while 1 == 1:
        computer_number = random.randint(1, 10)
        user_guess = int(input('Enter any number between 1 and 10: '))

        if user_guess == computer_number:
            print('You won')
        else:
            print('You got it wrong, you lost 1 life')
            user_lives -= 1
            print('You have {} live(s) remaining'.format(user_lives))
        if user_lives == 0:
            print('Game Over')
            break
print(five_lives(7))

