class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The class arrtibute is {self.a}")
        
o = Employee()
o.a = 66
o.show()