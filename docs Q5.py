# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

n={1:2,3:4,4:3,2:1, 0:0}
l=list(n.items())
l.sort()
print("Ascending Order:-",l)
l=list(n.items())
l.sort(reverse=True)
print("Descending Order:-",l)
dict=list(l)
print("Dictionary:-",dict)