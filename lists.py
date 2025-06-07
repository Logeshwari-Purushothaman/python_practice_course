#lists
#lists can have multiple data types
#lists can be empty

grocery_list = ['Apple','Milk','Brinjal','Berries','Pineapple']  # Example list of grocery items
data = ['Balachandra','18', True]  # List with mixed data types
emptylist = []  # An empty list

print('apple' in grocery_list)  # Check if 'apple' is in the grocery list
print('berries' not in grocery_list)  # Check if 'berries' is NOT in the grocery list
print(emptylist)  # Print the empty list
print(grocery_list.index('Brinjal'))  # Get the index of 'Brinjal' in the list
print(grocery_list[0:1])  # Print a slice of the list (first item as a sublist)
print(grocery_list[:4])  # Print the first four items in the list
print(grocery_list[-3:])  # Print the last three items in the list

print(len(grocery_list))  # Print the length of the grocery list
#to add an item to list
grocery_list.append('Sugar')  # Add 'sugar' to the end of the list
print(grocery_list)
#or you can do like below (1)
grocery_list+= ['Rice']  # Add 'rice' to the list using +=
print(grocery_list)
#or you can do like below (2)
grocery_list.extend(['Salt','Curry'])  # Add multiple items to the end of the list
print(grocery_list)

#to add a list to a another list
grocery_list.extend(data)  # Add all items from 'data' list to 'grocery_list'
print(grocery_list)

#extend add the items at the end
#use insert to add items with position
grocery_list.insert(0,'Chicken')  # Insert 'Chicken' at the beginning of the list
print(grocery_list)

#can also mention rate to insert an item with column range like 2:2
#if its in same range it wont replace by add the new item
grocery_list[1:1] = ['Curd']  # Insert 'Curd' at index 1 without replacing any items
print('\n')
print(grocery_list)

#if the range is not same but it has 2-3 elements it will replace old items with new item
grocery_list[1:5] = ['Tomato']  # Replace items from index 1 to 4 with 'Tomato'
print('\n')
print(grocery_list)

grocery_list.remove('Balachandra')  # Remove the first occurrence of 'Balachandra' from the list
print('\n')
print(grocery_list)

#removes the last element/index from the list
grocery_list.pop()  # Remove and return the last item from the list
print(grocery_list)

del grocery_list[1]  # Delete the item at index 1
print(grocery_list)

# #clears all the data inside the list variable
# grocery_list.clear()  # Remove all items from the list
# print(grocery_list)

#to sort items inside the list
#sort takes capital letters gives 1st preference by default
grocery_list.sort()
print(grocery_list)

grocery_list[1:2] = ['Orange']
print('\n')
print(grocery_list)

#it wont change letters to lower in the back it will change 
#and it sort based on it, when you print you wont see small letters
grocery_list.sort(key=str.lower)
print('\n')
print(grocery_list)


nums = [1,2,3,4,5,6,7,10,95,78,99,24,26]
nums.reverse()
print('\n')
print(nums)
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)


order = [1,56,78,95,34,98,34]
print(sorted(order,reverse=True))
print(order)

ordercopy = order.copy()
print('\n')
print(ordercopy)

#or u can also copy like below
ordercopy2 = order.copy()
ordercopy3 = list(order)
ordercopy4 = order[:]
print('\n')
print(ordercopy)
print(ordercopy2)
print(ordercopy3)
print(ordercopy4)

print(type(order))
