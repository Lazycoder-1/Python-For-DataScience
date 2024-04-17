# Difference in sets = elements not present in either of the sets
a = {1,2,3,4,5}
b = {4,5,6,7,8}
# using the difference method (-)
# Expected output - {1, 2, 3} 
c = a - b 

# using the .difference method
d = b.difference(a)

print(d)  