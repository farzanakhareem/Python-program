# Python program to display the Fibonacci sequence

def recursive_fibo(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibo(n-1) + recursive_fibo(n-2))

nterms =int(input("enter the value:  "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recursive_fibo(i))

