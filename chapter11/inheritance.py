class Employee:
    company = "Google"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")
        
        
        
class Programmer(Employee):
    company = "Google"
    def showLanguage(self):
        print(f"The name of the Employee is {self.name} and he is good with {self.language} language ")
        
a = Employee()
b = Programmer()

print(a.company, b.company) 