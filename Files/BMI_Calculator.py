# A simple BMI Calculator 
# BMI = weight(kg) * height(m)*2
user_weight = float(input('Enter your weight in kg: '))
user_height = float(input('Enter your height in meters: '))

results = user_height * (user_height)**2

print("Your BMI is " + str(results) +"kg/m^2") 