#For perfect no.
num = int(input("num="))
factor=[]
for i in range(1,num+1):
    if num%i==0:
        factor.append(i)
        print(i)
if num==sum(factor)-factor[-1]:
                print(factor,"\n It is a perfect no.")
