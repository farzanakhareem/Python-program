# Python program to reverse a number
#int is used to specify the input is integer


number = int(input("enter the number:"))
reverse = 0
a=number
while(number > 0):
	digit = number % 10
	reverse = reverse * 10 + digit
	number = number // 10

print("reverse of number" ,a," is",reverse)

-----------------------------------------------------------------------------




#we can find out the reverse of a number by slicing technique

#number = 123456
#print("reverse of number is",str(num)[::-1])



