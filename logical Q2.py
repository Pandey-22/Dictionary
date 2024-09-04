a=[[40,50,60],[70,80,90],[10,30,8]]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
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
i=0
while i<=8:
    print(i,":",p[i])
    i=i+1
    
    
# o/p=[40,50,60,80,90,10,30,8]
# {0:40,1:50,2:60,3:70,4:80,5:90,6:10,7:30,8:8}
# 0:40
# 1:50
# 2:60
# 3:70
# 4:80
# 5:90
# 6:10
# 7:30
# 8:8