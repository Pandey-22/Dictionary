dict={"a":21,"b":13,"c":25,"d":25}
for i,j in dict.items():
    print(i,":",j)




# a=[1,2,3,4]
# dict=c={}
# for i in a:
#     c[i]={}
#     c=c[i]
# print(dict)




# a={1:2,2:3,3:4}
# a.popitem()
# print(a)




# a={1:2,2:3,3:4}
# b=a.popitem()
# print(b)


# a={1:9,2:3,5:4}
# b=a.pop(2)
# print(b)



# a={1:9,2:3,5:4}
# a.pop(2)
# print(a)




# a={1:9,2:3,5:4}
# a.items()
# print(a)



# a={1:9,2:3,5:4}
# b=a.items()
# print(b)


# a={1:9,2:3,5:4}
# b=a.keys()
# print(b)



# a={1:9,2:3,5:4}
# b=a.values()
# print(b)



# a={1:9,2:3,5:4}
# b=a.get(2)
# print(b)



# a={1:9,2:3,5:4}
# a.get(2)
# print(a)



a="dular pandey"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)