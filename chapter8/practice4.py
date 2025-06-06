def Greatest(a, b, c):
    if(a > b and a > c):
        print("The greatest number is: ", a)
    elif(b > a and b > c):
        print("The greatest number is: ",b)
    elif(c >a and c >b):
        print("The greatest number is: ",c)

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
Greatest(a, b, c)