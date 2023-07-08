#counting no. of vowels

def count_vowels(a):
    #global v
    v = 0
    for i in a:
        if i.lower() in ["a","e","i","o","u"] :
            v  += 1
    return v
a = ("Hi Bro.")
print(count_vowels(a))
