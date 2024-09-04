# Q16.Write a Python program to map two lists into a dictionary.

d=["dular","kumari","pandey"]
d1=[2,5,6]
res={}
for i in d:
    for value in d1:
        res[i]=value
        d1.remove(value)
        break
print(str(res))