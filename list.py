# List slicing in Python
print("slicing")
my_list = ['p','r','o','g','r','a','m','i','z']

# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

print("-------------------------------------------------------------------------")

print("---------------updating the list----------------")

# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd)                   
print("--------------------------------------------------------------------------")
# Appending and Extending lists in Python
print("--------------Appending and Extending lists-------------")
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)


print("-----------------------------------------------------------------------------")
# Concatenating and repeating lists
print("---------Concatenating and repeating lists-----------")


odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)


print("-----------------------------------------------------------------------------")
print ("insert() method")

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]

print(odd)



print("-----------------------------------------------------------------------------")
print("--------delete/remove----------")

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)


print("--------------------------------------------------------------------")
print("some list method")


# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8))

# Output: 2
print(my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)
