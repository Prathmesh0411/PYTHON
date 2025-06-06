a = int(input("Enter the number of a:"))
b = int(input("Enter the number of b:"))
c = int(input("Enter the number of c:"))
d = int(input("Enter the number of d:"))

if(a>b and a>c and a>d):
    print("a is the greatest number which is ",a)
elif(b>a and b>c and b>d):
    print("b is the greatest number which is ",b)
elif(c>a and c>b and c>d):
    print("c is the greatest number which is ",c)
else:
    print("d is the greatest number which is ",d)