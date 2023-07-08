items=int(input("no. of items="))
dictionary={}
for i in range(items):
	key = int(input('Key='))
	value = int(input('Value='))
	dictionary[key]=value
print(dictionary.items())
