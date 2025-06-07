# Define lines for a formatted welcome message using strings
line1 = '********************************'
line2 = '                                '
line3 = 'Welcome to Python Programming!'
line4 = '                                '
line5 = '********************************'

# Print each line to display the welcome message in a box format
print(line1)
print(line2)
print(line3)
print(line4)    
print(line5)
# This code prints a welcome message in a formatted way

# The output will look like this:
# ********************************          
#                                
# Welcome to Python Programming!
#                                
# ********************************

# Assign a value to variable 'a'
a = 8

# Check if 'a' is greater than 10 using an if-else statement
if a > 10:
    print("a is greater than 10")
else:
    print("a is not greater than 10")   

# Use a ternary operator to print 'hi' if 'a' is greater than 10, otherwise print 'bye'
print('hi') if a > 10 else print('bye')


# Example 1: Without split()
# This will unpack each character of the input string into x, y, z, a
# If you enter '1234', x='1', y='2', z='3', a='4'
x, y, z, a = input("Enter the four values (without split, enter 4 characters): ")
print("Without split:", x, y, z, a)

# Example 2: With split()
# This will split the input string by spaces and assign each part to x, y, z, a
# If you enter '10 20 30 40', x='10', y='20', z='30', a='40'
x, y, z, a = input("Enter the four values (with split, space separated): ").split()
print("With split:", x, y, z, a)

