m={}
dic={"A":[4,6],"B":[9,6],"C":[3,5]}
for key,value in dic.items():
    n=[sum(value)]
    m[key]=n
print(m)