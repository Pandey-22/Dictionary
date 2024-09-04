# Q13.Write a Python program to sum all the items in a dictionary.

dict={"a":100,"b":200,"c":300}
sum=0
for i in dict.values():
    sum=sum+i
print("Sum=",sum)