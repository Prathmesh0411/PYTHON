class Employee:
    salary = 1000
    increment = 10    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100)) 
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 1200
print(e.increment)