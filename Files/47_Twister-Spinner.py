# Twister Spinner

import random
colors = ['red','blue','green']
body_choice = ['Right hand','Left hand','Right leg','Left leg']

spinner = random.choice(body_choice) + " ," + random.choice(colors) 
print('Twister Spinner says : ' + spinner)

