#Program to calculate Simple Interest
#User's input
a = int(input('''Select any number from given options below:
1. To find simple interest.
2. To find principle.
3. To find time.
4. To find rate.
5. To find amount.
'''))
#For finding simple interest
if a == 1:
    P = int(input("Principle(Rs) = "))
    T = int(input("Time (in years)= "))
    R = int(input("Rate (in %)= "))
    print("The S.I = Rs",(P*T*R)/100)
#For finding principle
elif a == 2:
    I = int(input("Interest(Rs) = "))
    T = int(input("Time (in years)= "))
    R = int(input("Rate (in %)= "))
    print("The Principle = Rs",(I*100)/(T*R))
#For finding time
elif a == 3:
    I = int(input("Interest(Rs) = "))
    P = int(input("Principle(Rs) = "))
    R = int(input("Rate (in %)= "))
    print("The Time = ",(I*100)/(P*R),"years")
#For finding rate
elif a == 4:
    I = int(input("Interest(Rs) = "))
    T = int(input("Time (in years)= "))
    P = int(input("Principle(Rs) = "))
    print("The Rate = ",(I*100)/(T*P),"%")
#For finding amount
elif a == 5:
    I = int(input("Interest(Rs) = "))
    P = int(input("Principle(Rs) = "))
    print("The Amount = Rs",P+I)
#For showing error to the user if he gives invalid input
else:
    print("Error! Enter a valid number.")
