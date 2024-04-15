
# removing elements from sets

numbers = {1,2,3,4,5,6}
# using the .discard() method 
#numbers.discard(5)

# using the .pop() method - removes element from the sets at random positions
letters_sets = set('Python')
letters_sets.pop()

# remove all elements from the set using the .clear() method
numbers.clear()
print(numbers)  