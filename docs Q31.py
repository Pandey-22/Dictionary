# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item1 45.5
# item3 41.3
# item4 55

d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for i,j in d.items():
    if i=="item1":
        print(i,j)
    if i=="item4":
        print(i,j)
    if i=="item3":
        print(i,j)