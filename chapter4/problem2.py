marks =[]
for i in range(6):
    m = int(input(f"Enter the marks of {i +1} student:"))
    marks.append(m)
    print(marks)
    marks.sort()
print(marks)