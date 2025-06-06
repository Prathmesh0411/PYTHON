def inches_to_cm(n):
    if(n == 0):
        return
    return n * 2.54

n = int(input("Enter a inches:"))
print(f"{n} inches is {inches_to_cm(n)} cm")