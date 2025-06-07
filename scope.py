#scope

name = "Balachandra" #global_variable
age = 22

def another():
        print('')
        global age  #to use global variable inside a local func
        age = age + 30
        def greeting(name):
            age = 30 #local_variable
            print(age)
            print(name)
        greeting("Share")

another()

def color():
        print('')
        global age  #to use global variable inside a local func
        age = age + 30
        print(age)
        color = 'blue'
        print(color)
        def greeting(name):
            age = 30 #local_variable
            nonlocal color #this will modify the locally assigned above variable which already local
            color = 'red'
            print(age)
            print(name)
            print(color)
        greeting("Share")
        print (color)

color()
