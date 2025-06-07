#numeric data types

#integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))
print('###################################################')

#float
gpa = 3.38
y = float(3.76)
print("this is",type(gpa))
print(isinstance(y,float))

print('###################################################')
#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print('###################################################')

#some of the integer functions
gpa = 3.2888
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,2))
print('###################################################')

import math
print(math.pi)
print(math.sqrt(989898))
print(math.sin(989898))
print(math.tan(989898))
print(math.factorial(64))

print('\n ###################################################')
zipcode = "10001"
zipcode = int(zipcode)
print(type(zipcode))

# error if you attempt to cast incorrect data
# zipcode = int("New York") 
# print(zipcode)

