# guessing game
import random
computer_num = random.randint(1,100)
user_num = int(input(('Enter a number: ')))

if user_num == computer_num:
    print('You are correct')
else:
    print('You are wrong')

print('The Computer guessed {}'.format(computer_num))
if computer_num > user_num:
    print('The computer guess was higher than your guess')
else:
    print('Your guess was higher than the computer guess')


