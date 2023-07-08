#write a python program to make a list of alphabets such that alphabets should multiply itself according to it's position.
a = []
for i in range(1,27):
    a.append(chr(i+96)*i)
print(a)
