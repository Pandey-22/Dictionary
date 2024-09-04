d={1:2,3:4,4:3,4:5,5:6,7:9,2:1,0:0}
l=list(d.items())
print("Ascending order=",l)
l=list(d.items())
l.sort(reverse=True)
print("Descending order=",l)
dict=dict(l)
print("Dictionary=",dict)