#Function to generate prime numbers
def check_prime(a):
    factor=[]
    for i in range(1,a+1):
        if a%i==0:
            factor.append(i)
    if len(factor)==2:
        print("prime")
    else:
        print("composite")
check_prime(int(input("Enter any number =")))
