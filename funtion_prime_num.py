#Function to prime numbers
def gen_prime(a):
                factor=[]
                for i in range(1,a+1):
                               if a%i==0:
                                               factor.append(i)
                                else:
                                                pass
                                if len(factor)==2:print(factor[1])
gen_prime(int(input("Enter any number =")))
