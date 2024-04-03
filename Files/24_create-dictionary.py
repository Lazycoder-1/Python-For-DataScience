# creating dictionaries , key-value pair {name:'John'}

items = {'ps5':2000,'macbook':4000}

#print(items)

# using lists in dictionaries
#numbers = {1:'ID',2:[2,3,4,5]}
#names = ['Ohene','Karl','Nick']
#ages = [25,23,31]
#combined_list = list(zip(names,ages)) using the zip will return names and ages as combined list objects
#print(combined_list)

# turning lists objects to dictionaries , using zip and dict methods as below
names = ['Ohene','Karl','Nick']
ages = [25,23,31]
combined_dict = dict(zip(names,ages))
print(combined_dict)
