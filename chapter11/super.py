class Employee:
    def __init__(self):
        print("Constructor for employee")
    a = 1
        
class Programmer(Employee):
    def __init__(self):
        print("Constructor for programmer")
    b = 2
 
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor for manager")
    c = 3 

o = Manager()
print(o.a, o.b, o.c)      