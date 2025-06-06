def great(a,b,c):
    if(a > b and a > c):
        print(f"a is the greatest number:{a}")
    elif(b > a and b > c):
        print(f"n is the greatest number: {b}")
    elif(c > a and c > b):
        print(f"c is the greatest number: {c}")
        
        
a  = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))       
great(a,b,c)