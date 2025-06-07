mytuple = tuple(('Dave',43, True))

anothertuple = (1,2,2,2,4,6,8,10)

print(mytuple)
print(anothertuple)
print(type(mytuple))
#we cannot change items inside tuple as they are immutable
#if we want to add an item
#we can change tuple to list and add an item and again change to tuple
#this is called packaging
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print((newtuple))

#to unpack a tuple
(one,two,*hey,three) = anothertuple
print('\n')
print(one)
print(two)
print(hey)
print(three)

print(anothertuple.count(2))