l=[1,2,3,4,5,6,7,8,9,-11,-12,-13,-14,-15]
post_count=1
n=0
sum_neg=0
b=[]
while n<len(l):
    if l[n]>=0:
        post_count+=1
    if l[n]<=0:
        sum_neg=sum_neg+(l[n])
    n=n+1
b.append(post_count)
b.append(sum_neg)
print(b)