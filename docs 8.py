# Write a Python program to check whether a given key already exists in a dictionary.

d={1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80,9:90}
a=int(input("enter any number--"))
if a in d:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")