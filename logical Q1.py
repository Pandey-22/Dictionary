a={1:2,2:3,3:4,4:8,5:5,6:9,7:6,8:9,9:7}
max=0
max_k=None
d={}
for i in a:
    if a[i]>max:
        max=a[i]
        max_k=i
d[max_k]=max
print("Max_Key=",max_k)
print("Maxmun=",max)
print("Max key and Max value=",d)