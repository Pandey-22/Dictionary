a=[[40,50,60],[70,80,90],[10,30,20]]
i=0
b=[]
while i<len(a):
    if type(a[i]==type([])):
        j=0
        while j<len(a):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a):
                    b.append(a[i][j][k])
                    k=k+1
            else:
                b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)
p={}
i=0
while i<len(b):
    p[i]=b[i]
    i=i+1
print(p)