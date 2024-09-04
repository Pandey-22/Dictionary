a={{"math":90,"science":92,},{"math":89,"science":94},{"math":92,"science":88}}
d=input("enter the number..")
l=[]
for i in a:
    for j in i:
        if j==d:
            s=i[j]
            l.append(s)
print(l)

