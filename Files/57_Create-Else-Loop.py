# creating loops with the else statements with the break method
items = 'apples'
shopping_items = ['mango','kiwi','strawberry','eggnog','apples']
for item in shopping_items:
    if item == items:
        print(item +" is the list")
        break
else:
    print('Item not found')