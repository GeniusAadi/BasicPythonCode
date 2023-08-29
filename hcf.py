#Program to find HCF of two numbers
#Function to find HCF
def hcf(a,b):
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
    return large
a=int(input("Enter 1st num= "))
b=int(input("Enter 2nd num= "))
ans=hcf(a,b)
print("HCF=",ans)