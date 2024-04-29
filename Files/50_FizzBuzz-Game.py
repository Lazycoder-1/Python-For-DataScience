# FizzBuzz game with for loops
start = 1
stop = 17
for i in range(start,stop):
    if i % 5== 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

