#sets
#no duplicates allowed

nums = {1,2,3,4}
num2 = set((1,2,3,4))


print(nums)
print(num2)
print(type(nums))
print(len(nums))

#duplicates removed
nume = {1,2,2,2,3,3}
print(nume)

#true is a dupe of 1, false is a dupe of 0
num3 = {1,True,3,4,False,0,0}
print(num3)

#check if a value is in a set
print(1 in num3)

#you cannot refer to an element in the set with an index position or a key


#how to add a new element to a set
num3.add(8)
print(num3)

#add elements from one set to another
morenum = {5,6,7}
num3.update(morenum)
print(num3)


#you can use update with lists, tuples and dictionaries too

#merge two sets to create a new set
one = {1,2,3}
two = {2,3,5,6,7}
print("----------")
#mynewset= one.union(two)


one.intersection_update(two)
print(one) #keeps only the duplicates

#keep everything except duplicate
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)

