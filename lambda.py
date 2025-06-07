#lambda 
squared = lambda num : num * num
print(squared(3))

#sum = lambda num : num  + 2 
print(sum(3))

#sum = lambda a,b : a + b 
print(sum(2,3))

def funcBuilder(y):
    return lambda a : a * y


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(20))



#--------------------------
##---higher order functions
##map
##filter

print("------------------------")

numbers = [3, 7, 12, 18, 20, 21]

squared_numbers = map(lambda num : num * num, numbers)
print(list(squared_numbers))

odd_number = filter(lambda num : num % 2 != 0,numbers)
print(list(odd_number))


#-----------------------
from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc,curr: acc + curr, numbers,5)
print(total)
print(sum(numbers,12))


names = ['Dave', 'Balachandra', 'Gray','Suresh']
char_count = reduce(lambda acc,curr: acc + len(curr),names,0)

print(char_count)