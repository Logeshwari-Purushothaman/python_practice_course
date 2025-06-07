#recursion
#function call inside a function 

def add_one(num):
    if (num >= 9):
        return num+1
    total = num + 1
    print(total)

    return add_one(total) #again and again inside function

mynewtotal = add_one(0)
print(mynewtotal)

print("-----------------------------------------")
#program to print factorial of a number recursively

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)

num = 3

#check if the input is valid or not 
if num < 0:
    print('Invalid input')
elif num == 0:
    print("factorial of 0 is 1")
else:
    print("factorial of ", num, "=", recursive_factorial(num))