
# a simple game where a user loses lives when he guess wrong answer
import random
user_lives = 5
# conditions
while 'ohene' == 'ohene':
    computer_number = random.randint(1, 10)
    user_guess = int(input('Enter any number between 1 and 10: '))
    if user_guess == computer_number:
        print('Voala, You won')
        break
    else:
        print('You got it wrong, you lost 1 life')
        user_lives -= 1
        print('You have {} live(s) remaining'.format(user_lives))
    if user_lives == 0:
        print('Game Over')
        break

print('The computer guess was ' + str(computer_number))





