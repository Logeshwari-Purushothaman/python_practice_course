#loops
#while loop
# break -completely comes out of loop
#continue - will restart from top of loop 
i = 1
while i <2:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i is no longer less than 10")


print("----------")

#for loop
fruits = ["Apple","Orange","Mango"]
for x in fruits:
    if x == "Orange":
        continue
    print(x)

for x in "Share":
    print(x)

print("----------")

for x in range(10):
    print(x)

print("----------")

for x in range(2,4):
    print(x)


#to increase range 0 to 101 by 5
for x in range(0,101,5):
    print(x)
else:
    print("Glad its over")

#nested loop
names = ["Balachandra", "Dave","Ganesh"]
actions = ["code","eats","sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")


