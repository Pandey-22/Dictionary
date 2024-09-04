# Q46.A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary. 
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

d1={'C1':[10,20,30],'C2':[20,30,40],'C3':[12,34]}
a={}
for i,j in d1.items():
    j.clear()
    a.setdefault(i,j)
print(a)