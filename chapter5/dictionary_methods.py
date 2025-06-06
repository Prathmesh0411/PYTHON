marks = {
    "prathmesh":100,
    "umesh":101,
    "yadav":102
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"prathmesh": 99})
print(marks)

print(marks.get("prathmesh")) #returns None if key not found
print(marks["prathmesh"]) #returns keyerror if key not found
print(len(marks))