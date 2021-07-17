"""from math import sqrt
*/ssssssd/*
print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()
	"""
#-------------------------------------------------------------------------------------------
				#another method including complex number

# Python program to find roots of quadratic equation

import math  #importing math-module

# take inputs
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))

# calculate discriminant
dis = (b**2) - (4*a*c)

# checking condition for discriminant
if(dis > 0):
    root1 = (-b + math.sqrt(dis) / (2 * a))
    root2 = (-b - math.sqrt(dis) / (2 * a))
    print("Two distinct real roots are %.2f and %.2f" %(root1, root2))

elif(dis == 0):
    root1 = root2 = -b / (2 * a)
    print("Two equal and real roots are %.2f and %.2f" %(root1, root2))

elif(dis < 0):
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-dis) / (2 * a)
    print("Two distinct complex roots are %.2f+%.2f and %.2f-%.2f" 
                          %(root1, imaginary, root2, imaginary))
