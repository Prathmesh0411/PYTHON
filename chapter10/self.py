class Employee:
    language = "Python"
    salary = 12000000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")
        
    @staticmethod
    def greet():
        print("Good morning!")
        

harry = Employee()
harry.language = "javascript"
harry.greet()
harry.getInfo()     