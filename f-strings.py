person = "Balachandra"
coins = 3


#concatenate strings
print("\n"  + person + " has" + str(coins) + " coins left")

#####previous %s formatting
message = "\n %s has %s coins left." % (person,coins)
print(message)

#########previous string.format() method

message = "\n{} has {} coins left".format(person,coins)
print(message)


message = "\n{person} has {coins} coins left".format(
    coins = coins, person = person)
print(message)

player = {'Person' : 'Dave', 'Coins' : 3}

message = "\n{Person} has {Coins} coins left".format(**player)
print(message)


#---------------------------------------------------
#f-strings! This is the way

message = f"\n{person} has {coins} coins left"
print(message)


message = f"\n{person.lower()} has {2 * 4} coins left"
print(message)


message = f"\n{player['Person']} has {2 * 4} coins left"
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.1f}\n")

for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25 * num:.3f}")
    print(f"2.25 divided by {num} is {2.25 / num:.3%}\n")


