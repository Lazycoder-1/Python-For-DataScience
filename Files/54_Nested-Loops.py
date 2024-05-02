# working with nested loops - for and while loops
# for a in ['I play ','I watch ','I enjoy ']:
#     for b in ['soccer','baseball','basketball']:
#         print(a + b)

# expected results :
# I play soccer
# I play baseball
# I play basketball
# I watch soccer
# I watch baseball
# I watch basketball
# I enjoy soccer
# I enjoy baseball
# I enjoy basketball


# complex scenario
a = 1
b = 1
while a <= 3:
    print('This is the outer loop number {}'.format(a))
    while b <= 5:
        c = a * b
        print('Inner loop number {} calculates {} * {} = {}'.format(b,a,b,c))
        b += 1
    a += 1
    b = 1
    print('___')