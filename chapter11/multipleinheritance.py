class Employee:
    company = "Google"
    name = "Default Name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
        
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "Google"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} Language")
        
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
