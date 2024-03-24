# remove elements from lists
lifestyle = ['eat','survey','eat','code','sleep']
lifestyle.remove('eat')
#print(lifestyle)

# using the pop method to remove elements from the list
# pop - removes the last element in the list
p_languages = ['php','html','swift','java','css','laravel','python']
p_languages.pop(-3)
p_languages.pop(1)
n_languages = p_languages

#print(n_languages)

# example , using the append method
coding_languages = ['php','html','swift','java','css','laravel','python']
r_1= coding_languages.pop(-3)
r_2 = coding_languages.pop(1)

print(r_1,r_2)