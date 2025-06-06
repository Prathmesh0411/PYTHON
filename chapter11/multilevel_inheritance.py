class Employee:
    a = '*'
class Programmer(Employee):
    b = '*'
class Manager(Programmer):
    c = '*'
    
o = Employee()
print(o.a)

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)