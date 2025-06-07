
##try catch block
x = 2
try:
    print(x)
except Exception as PAIN:
    print("error")
except Exception as error:
    print(error)
else: #this is executed as default after try
    print("No errors")
finally:
    print("I'm going to print with or without an error.")
    