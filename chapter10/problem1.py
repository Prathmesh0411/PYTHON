class Programmer:
    company = "Google"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Prathmesh", 1300000, 411048)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 1200000, 586209) 
print(r.name, r.salary, r.pin, r.company)       