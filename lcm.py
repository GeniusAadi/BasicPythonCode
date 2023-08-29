#Python program to find LCM
#Function to find LCM
def lcm(a,b):
    if a>b:
        large=a
        small=b
    elif b>a:
        large=b
        small=a
    else:
        large=small=a=b
    r=1
    while r>0:
        r=large%small
        large=small
        small=r
    l=a*b/large
    return l
a=int(input("Enter 1st num= "))
b=int(input("Enter 2nd num= "))
ans=lcm(a,b)
print("LCM=",ans)