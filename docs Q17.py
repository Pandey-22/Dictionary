# Q17.Write a Python program to sort a dictionary by key.

color_dict = {'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
for key in sorted(color_dict):
    print(key, color_dict[key])