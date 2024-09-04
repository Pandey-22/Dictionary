# Q41.Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

d={'Cierra Vega':12,'Alden Cantrell':12,'Kierra Gentry':12,'Pierre Cox':12}
for i,j in d.items():
    if j==12:
        print("True")
    elif j==10:
        print("False")