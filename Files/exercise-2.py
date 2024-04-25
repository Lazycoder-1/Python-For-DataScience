
# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

# Temperature from Celsius to Fahrenheit 
# C to F =  °F = (°C × 9/5) + 32
# F to C = °C = (°F − 32) x 5/9 

temperature_c = float(input('Enter a temperature in Celsius: '))
temperature_f = float(input('Enter a temperature in Fahrenheit: '))

# convert from celsius to fahrenheit
temperature_converted = (temperature_c * (9/5)) + 32
temperature_converted_f = (temperature_f - 32) * (5/9)

print(str(temperature_converted) +''+'F') 
print(str(temperature_converted_f) +''+'C') 



