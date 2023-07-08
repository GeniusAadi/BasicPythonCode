#Fibonancy series
a = int(input("Enter any number to see fabonancy series = "))
b = 0
c = 1
print(b)
print(c)
'''while b < a:
                s = b + c
                b = c
                c = s
                print(s)'''
for i in range(b,a+1):
                s = b + c
                b = c
                c = s
                print(s)
