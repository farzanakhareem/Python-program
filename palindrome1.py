# function which return reverse of a string


s = input("enter the string:")
ans = s[::-1]

if ans==s:
	print("Yes,string is palindrom")
else:
	print("No,string is not palindrom")


#----------------------------------------------------------------------------------------------

# another method for palindrom with function

#def isPalindrome(s):
#	return s == s[::-1]


#s = input("enter the string:")
#ans = isPalindrome(s)

#if ans:
#	print("Yes")
#else:
#	print("No")

