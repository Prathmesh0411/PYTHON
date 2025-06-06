class Employee:
    a = 2
    @classmethod
    def show(cls):
        print(f"Class attribute a: {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = Employee()
e.a = 4
e.show()

e.name = "prathmesh Rathod"
print(e.name)