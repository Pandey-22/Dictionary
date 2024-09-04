# Q14.Write a Python program to multiply all the items in a dictionary.

dict={"n":10,"m":7,"x":2}
mul=1
for i in dict.values():
    mul=mul*i
print(mul)