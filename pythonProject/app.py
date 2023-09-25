# Import math is trying to input some variable from the math library
import math
#Using a,b,c and input is assigning and also collecting the variable from the user
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
#-b+b**2-4*a*c/2*a

x1=(-b+math.sqrt(b**2-4*a*c))/2*a
x2=(-b-math.sqrt(b**2-4*a*c))/2*a

print(x2)