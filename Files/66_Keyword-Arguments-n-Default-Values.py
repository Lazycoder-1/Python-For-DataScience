
# Keyword arguments and default values
# here we specify the items for the parameters and arguments to the function

def contact(name,email):
    message = 'Hi {}, Your new email is {}'.format(name,email)
    return message
print(contact(email='deansmith@gmail.com',name='Dean'))

# it does not matter the order we passed in the arguments here
# this makes the order of assignment easier and understandable


