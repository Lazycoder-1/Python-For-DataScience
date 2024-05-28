
# Parameters and Arguments
# the parameter here is (name)
# the argument here is ('Dean')

# def contact(name):
#     message = 'Hi {}, how are you today'.format(name)
#     return message
#
# print(contact('Dean'))



# Another scenario with 2 parameters and arguments
# Parameters and Arguments
# the parameter here is (name,email)
# the argument here is ('Dean','deangreen@gmail.com)

def contact(name,email):
    message = 'Hi {}, Your new email is {}'.format(name,email)
    return message

print(contact('Dean','deangreen@gmail.com'))