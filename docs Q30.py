product_dic={"S  001":['Math', 'Science'],"S    002":['Math', 'English']}
product_dic={x.replace(" ",""):v for x,v in product_dic.items()}
print("New Dictionary",product_dic)