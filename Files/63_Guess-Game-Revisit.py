
import random
computer_guess = random.randint(1,100)
#print(computer_guess)
while 'play' == 'play':
    user_guess = int(input('Enter a number: '))
    if user_guess == computer_guess:
        print('Boom, You win')
        #print('Another challenge')
        break
    elif user_guess > computer_guess:
        print('Your guess was greater than the computer guess')
    elif user_guess < computer_guess:
        print('Your guess was lower than the computer ')
    else:
        print('Ooops, try again')

print('The computer guess was ' + str(computer_guess))


