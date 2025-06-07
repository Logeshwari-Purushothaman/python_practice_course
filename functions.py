#functions

def hello_world():
    print("Hello world")

hello_world()

def sum(num1,num2):
   if (type(num1) is not int or type(num2) is not int):
      return 
   return num1 + num2

print(sum(9,10))


#*agrs takes as many as parameters
def multiple_items(*args):
   print(args)
   print(type(args))

multiple_items("Dave","John","Saara")

def add(*num):
   sum = 0
   for n in num:
    sum = sum + n
   print("Sum:",sum)
   
add(2,6)

def multi_named_items(**kwargs):
   print(kwargs)
   print(type(kwargs))

   
multi_named_items(first ="Subscribe",last="Share")

def samp(a,b,*args, option = False, **kwargs):
   print('')
   print(a,b)
   print(args)
   print(option)
   print(kwargs)

samp(1,2,3,10,20,50, Name = 'Tom',Salary = 60000)
