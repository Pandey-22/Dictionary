# Q15.Write a Python program to remove a key from a dictionary.

dict={"name":"DularPandey","age":15,"study":"coding"}
print(dict)
k=input("enter the key---")
if k in dict:
    del dict[k]
else:
    print("Given key is not in this dictionary")
print("\nUpdated Dictionary=",dict)