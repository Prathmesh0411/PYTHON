def sum(n):
    if(n == 1):
        return 1
    return sum(n - 1) + n

n = int(input("Enter a number:"))
print(f"sun to first {n} numbers is {sum(n)} ")