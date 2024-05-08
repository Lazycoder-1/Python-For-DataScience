# a simple function
def rating(sales):
    if sales >= 50000:
        print('Gold status')
    elif sales >= 10000:
        print('Silver status')
    elif sales >= 1000:
        print('Bronze status')
    else:
        print('Better luck next time')

rating(60000)