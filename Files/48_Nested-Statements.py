
# Example: Find a greater number between two numbers

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
# nested condtion statements 
if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is greater than', num2)
else:
    print(num1, 'is smaller than', num2)

