# Q47.Write a Python program to find the length of a given dictionary values. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

d1={1:'red',2:'green',3:'black',4:'white',5:'black'}
r={}
for i in d1.values(): 
    r[i] = len(i)  
print("Length of dictionary values:")
print(r)