# lists slicing , i.e selecting where you want to start and end the list indexes.
# eg, to select from classic to old school, music[0:4] , still 0 basis on the index

music = ['classic','hip pop','edm','old school','rnb','reggae','afrobeat']
fav = music[0:4]
other = music[4:7]

#shorthands for both scenarios
fav_1 = music[:4]
other_1 = music[4:]

# different methods, the steps or the order in which it should start i.e 2,3,4 etc
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::2])

