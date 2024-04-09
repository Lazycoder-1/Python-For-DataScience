# other dictionary methods
# using the .items method
shopping_items = {'ps5':2500,'macbook':4000,'console':1000,'sneakers':500}
new_items = shopping_items.items()
#print(type(new_items))

# how to access the keys 
# Expected output    dict_keys(['ps5', 'macbook', 'console', 'sneakers'])
#print(shopping_items.keys())

# how to access the values
# Expected output   dict_values([2500, 4000, 1000, 500])
#print(shopping_items.values())

# using the for loops for iteration
# iterating through the values
for value in shopping_items.values():
    print(value)
print('\n')
# iterating through the keys
for key in shopping_items.keys():
    print(key)
print('\n')
# iterating through the entire dictionary
#for item in shopping_items.items():
    #print(item)