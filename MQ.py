# t_d={"dular":1,"pandey":2,"pooja":3,"pandey":4}
# print("The original dictionary:"+str(t_d))
# d={}
# for val in t_d:
#     if t_d[val] in d:
#         break
#     else:
#         d[t_d[val]]=1
# print("Does dictionary contain repetition:"+str(d))




# t_d={"Gfg":1,"is":3,"Best":2}
# print("The original dictionary is:"+str(t_d))
# res=list(t_d.keys())+list(t_d.values())
# print("The ordered keys and values:"+str(res))



# a={"a":1,"b":2,"c":3,"d":4}
# for i in a.keys():
#     print(i)
# for j in a.values():
#     print(j)




# d={{"first":"1"},{"second":"2"},{"third":"1"},{"four":"5"},{"five":"5"},{"six":"9"}}
# i=0
# a=[]
# while i<len(d):
#     for j in d[i]:
#         if d[i][j] not in a:
#             a.append(d[i][j])
#     i=i+1
# for i in d:
#     print(a)



dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
d={}
for i,j in dic.items():
    if j not in d.values():
        d[i]=j
print(d)