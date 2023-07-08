#Finding roots of the quadratic equation
import math
a = int(input("Enter a number except 0 = "))
b = int(input("Enter another number  = "))
c = int(input("Enter another number = "))
d = b**2-4*a*c
print("The quadratic equation is ",a,"x^2+",b,"x+",c,"=0")
if d < 0:
    print("The solution is an imaginary number.")
elif d == 0:
    sq = math.sqrt(d)
    print("The solution is ",(-b+sq)/(2*a))
    print("The other solution is " ,(-b-sq)/(2*a))
else:
    sq = math.sqrt(d)
    print("The solution is ",(-b+sq)/(2*a))
    print("The other solution is " ,(-b-sq)/(2*a))
