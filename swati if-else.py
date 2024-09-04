#  Accept the number of days from the user and calculate the charge for library according to following :
# First five days : Rs 2/day.
# Six to ten days  : Rs 3/day.
# Ten to 15 days  : Rs 4/day
# After 15 days    : Rs 5/day

a=int(input("enter the number"))
if a>=1 and a<=5:
    print(2)
elif a>=6 and a<=10:
    print(3)
elif a>=11 and a<=15:
    print(4)
else:
    print(5)