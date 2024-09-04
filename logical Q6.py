a="HELLO! pandey!"
i=0
n=""
while i<len(a):
    if a[i]>="A" and a[i]<="Z":
        c=a[i].lower()
        n=n+c
    else:
        d=a[i].upper()
        n=n+d
    i=i+1
print(n)