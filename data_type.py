first_name = "Logeshwari"
last_name = "Purushothaman"
#literal assignment
print(type(first_name))  
print(type(first_name) == str)
print(isinstance(first_name,str))
#constructor assignment
new_name = str("Click the bell button")
print(type(new_name))
print(type(new_name) == str)
print(isinstance(new_name,str))


#concatenate
full_name = first_name + last_name + '\tFemale'
print(full_name)
#casting
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like dancing from " + decade + " year"
print(statement)

#use three single colon for multi line 
multi_line = '''
Hello
welcome
to 
class'''

print('###################################################')
print(multi_line)
###################################################
sentence = 'I\'am logeshwari \t welcome \n to my class!'
print(sentence)
print(sentence.lower())
print(sentence.upper())
print(sentence.isascii())
print(sentence.isnumeric())

print('###################################################')
print(sentence.replace('to','FOR'))

print(len(sentence))
sentence += "1234567890"
print(len(sentence))
sentence1="  this is a example    "
print(len(sentence1))
###################################################
#to remove white spaces in beginning and in end
print(sentence1.strip())
print(sentence1.lstrip())
print(sentence1.rstrip())

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Bluberrcake".ljust(16,".") + "$12".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

print('###################################################')
first = 'Subscribe'
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean data
print(first.startswith('S'))
print(first.endswith('e'))









