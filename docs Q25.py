# students={"Aex":{"class":"V","roll_id":12},"Puja":{"class":"V","roll_id":3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print(b,":",students[a][b])


c={'w':1,'3':1,'r':2,'e':2,'s':1,'o':1,'u':1,'c':1}
w='w3resource'
for i in w:
    if i=="w":
        c["w"]=c["w"]+1
    elif i==3:
        c[3]=c[3]+1
    elif i=="r":
        c["r"]=c["r"]+1
    elif i=="e":
        c["e"]=c["e"]+1
    elif i=="s":
        c["s"]=c["s"]+1
    elif i=="o":
        c["o"]=c["o"]+1
    elif i=="u":
        c["u"]=c["u"]+1
    elif i=="r":
        c["r"]=c["r"]+1
    elif i=="c":
        c["c"]=c["c"]+1
    elif i=="e":
        c["e"]=c["e"]+1
print(c)