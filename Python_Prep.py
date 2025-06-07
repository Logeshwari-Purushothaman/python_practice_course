#1.Converting an Integer into Decimals
value = 123
word = int(value)
print(type(word))
print("'''''''''''''''''''''''''''''''''\n")

#2. Converting an String of Integers into Decimals
Word = "123"
Value = int(Word)
print(type(word))
print("'''''''''''''''''''''''''''''''''\n")

#3.Reversing a String using an Extended Slicing Technique
string = "Python Programming" 
print(string[::-1])
print("'''''''''''''''''''''''''''''''''\n")

#4.Counting VOWELS in a Given Word
vowel = [ 'a', 'e', 'i', 'o', 'u'] 
word= "programming"
count= 0
for character in word:
  if character in vowel: 
    count += 1
print(count)
print("'''''''''''''''''''''''''''''''''\n")

#5.Counting CONSONANTS in a Given Word
vowel = [ 'a', 'e', 'i', 'o', 'u'] 
word= "programming"
count= 0
for character in word:
  if character not in vowel: 
    count += 1
print(count)
print("'''''''''''''''''''''''''''''''''\n")

#6. Writing FIBONACCI Series
fib = [0,1]
# Range starts from g by default
n=5
for i in range(n): 
  fib.append(fib[-1] + fib[-2])
#Converting the List of integers to string
print(', '.join(str(e) for e in fib))
print("'''''''''''''''''''''''''''''''''\n")


#7. #Finding the Maximum Number in a list
numberlist = [12, 3, 55, 23, 6, 78, 33, 4]
max = numberlist[0]
for num in numberlist:
  if max < num:
    max = num 
print(max)
print("''''''''''''''''''''''''''''''''\n")


#8. Finding the Minimum Number in a List
numberlist = [12, 3, 55, 23, 6, 78, 33, 4]
min= numberlist[0]
for num in numberlist:
  if min> num:
    min= num 
print(min)
print("''''''''''''''''''''''''''''''''\n")


#9. Finding the middle Element in a list
numList = [12, 3, 55, 23, 6, 78, 33, 5]
midElement = int((len(numList)/2)) 
print(numList[midElement])
print("'''''''''''''''''''''''''''''''\n")


#11.Converting a list into a string
list= ["P", "Y", "T","S","R"]
string= "".join(list)
print(string) 
print(type(string))
print("'''''''''''''''''''''''''''''''\n")

#13.Comparing Two Strings for ANAGRAMS
strl = "Listen" 
str2 = "Silent"
strl = strl.replace(" ","").upper()
str2 = str2.replace(" ","").upper()

if sorted(strl) == sorted(str2): print("True")
else:
  print("False")
print("'''''''''''''''''''''''''''''''\n")


#14. Checking for PALINDROME Using Extended Slicing Technique
str1 ="Kayak".lower()
print(str1)
print(str1[::-1])
if str1 == strl[::-1]: 
  print("True")
else:
  print("False")
print("'''''''''''''''''''''''''''''''\n")


#15.Removing All Whitespace in a String
string="C O D E"
string2 =string.replace(" ","")
print(string2)
print("'''''''''''''''''''''''''''''''\n")


#19.Building a Pyramid in Python
def pyramid(n):
    for i in range(n):
        for j in range(i, n): 
            print(" ", end="")        # print leading spaces
        for j in range(i + 1): 
            print("*", end="")        # left half of stars
        for j in range(i): 
            print("*", end="")        # right half of stars
        print()                       # move to next line (INSIDE loop)

pyramid(10)
