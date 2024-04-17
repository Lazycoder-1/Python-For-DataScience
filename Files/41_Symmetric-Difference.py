# the symmetric difference is the opposite of intersection operation 
# represented by ^

a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = a ^ b 

# using .symmetric_difference method
d = a.symmetric_difference(b)

print(d)  