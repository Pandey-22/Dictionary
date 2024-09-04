# Q37.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

d={'c1':'Red','c2':'Green','c3':None}
d.pop("c3")
print("New Dictionary--",d)