# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}

list=[1,2,3,4]
dict=c={}
for n in list:
    c[n]={}
    c=c[n]
print(dict)