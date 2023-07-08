people=int(input("Total no. of people="))
lst=[]
for i in range(people):
	a = input("Name=")
	lst.append(a)
for j in lst:
	if j.startswith("A"):
		print(j)
