# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

fruits={"strawberry":20,"apple":300,"banana":50,"papaya":40,"mango":65}
costly_fruits=sorted(fruits, key=fruits.get,reverse=True)
for i in range(3):
    print(costly_fruits[i])