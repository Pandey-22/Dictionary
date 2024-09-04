# Q50.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

d1={'V':[1,4,6,10],'VI':[1,4,12],'VII':[1,3,8]}
b={}
for i,j in d1.items():
    j.remove(1)
    b.setdefault(i,j)
print(b)