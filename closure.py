#closure

#closure is a function having access to the scope of its parent function after the parent function has returned

def parent_function(person,coins):
    #coins = 3
    def play_name():
        nonlocal coins 
        coins = coins - 1
        if coins > 1:
            print("\n")
            print( person + "has"+ str(coins) + "coins left" )
        elif coins == 1:
            print( person + "has"+ str(coins) + "coins left" )
        else:
            print(person + "is out of coins")
    return play_name

tommy = parent_function("Tommy",5)
jenny = parent_function("Jenny",10)

tommy()

tommy()
tommy()
jenny()


print("---------------------------------------------")

def make_multiplier_of(n):
    def multiplier(x):
        print(x)
        print(n)
        return x * n
    return multiplier

times2= make_multiplier_of(6)
times5= make_multiplier_of(3)

print(times2(9))
