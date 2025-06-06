class Employee:
    language = "Python"
    salary = 12000000
    
    
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("im creating an object")
        
        
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")
        
    @staticmethod
    def greet():
        print("Good morning!")
        

harry = Employee("Prathmesh",1300000,"Python")
print(harry.name,harry.salary,harry.language)
# harry.language = "javascript"
harry.greet()
harry.getInfo()     

# harry = Employee()