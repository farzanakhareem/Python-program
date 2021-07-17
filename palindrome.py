# Program to check if a string is palindrome or not

my_string = 'aIbohPhoBiA'
my_string = input("enter the string:")

# make it suitable for caseless comparison

my_string = my_string.casefold()

# reverse the string
rev_str = reversed(my_string)

# check if the string is equal to its reverse
if list(my_string) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

