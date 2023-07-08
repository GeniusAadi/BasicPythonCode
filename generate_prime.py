#To generate prime no.
lim = int(input("num= "))
for i in range(2,lim+1):
    half = lim//2 + 1
    c = 0
    for j in range(2,i):
        if i%j==0:
            c+=1
if c == 0:
    print(lim,"is prime no.")
else:
    print(lim,"is composite no.")