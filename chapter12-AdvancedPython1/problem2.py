# write a program to print third, fifth and seventh element from a list using enumerate function
l = [ 1, 3, 4, 2, 5, 6, 5, 6, 9, 8, 7]

for i, item in enumerate(l):
    if i ==2 or i ==4 or i ==6:
        print(item)
        
        