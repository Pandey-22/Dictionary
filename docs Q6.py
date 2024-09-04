# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d={0:10,1:20}
print("Original Dictionary:--",d)
d.update({2:20})
print("Expected Result:--",d)