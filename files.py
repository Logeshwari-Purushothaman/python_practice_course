import os
#rawx
#r = read
#a = append ##writes new
#w = write  ## replaces existing content
#x = Create

#Read = error is it doesn't exist

f = open("C:\\Users\\loges\\Documents\\python_refresh\\names.txt")

for x in f:
    print(x)


# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

f.close()


try:
    f = open("C:\\Users\\loges\\Documents\\python_refresh\\names.txt")
    print(f.read())
except:
    print("File is not there")
finally:
    f.close()


f= open("names.txt","a")
f.write("\nComment")
f.close()

f = open("context.txt","w")
f.write("Replace this content")
f.close()

f = open("context.txt")
print(f.read())
f.close()


##2 ways to create a new file

#1. open a file and creates a file if doesnt exit

f = open("list.txt","w")
f.close()


#2. creates  a specified file but returns error if the file
if not os.path.exists("dave.txt"):
    f = open("dave.txt","x")
    f.close()


#delete a file if it exists to avoid an error
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("File doesnt exist")


# with has built-in implicit exception handling
#close() will be automatically called

with open("context.txt") as f:
    content = f. read()

with open("names.txt", "w") as f:
    f.write(content)