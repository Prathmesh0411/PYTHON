a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
result = int(a / b)
if(a % b != 0):
    print(f"The result is {result} and reminder is {a % b}")
else:
    print(f"Thw result is {result}")