a = int(input("Enter a number:"))
b = int(input("Enter b number:"))

if(b == 0):
    raise ZeroDivisionError("Heyyyy give valid number")
else:
    print(f"The division a/b is{a/b}")