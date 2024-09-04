# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

d={"a":5,"b":2,"c":8}
max_key=max(d,key=d.get)
min_key=min(d,key=d.get)
print("Max=",max_key)
print("Min=",min_key)