class calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}.")
        
    def cube(self):
        print(f"The cube of {self.n} is {self.n * self.n * self.n}.")
        
    def squareroot(self):
        print(f"The square root of {self.n} is {self.n**(1/2)}.")
    
    @staticmethod
    def greet():
        print("Hello!")
        
a = calculator(8)
a.greet()
a.square()
a.cube()
a.squareroot()
        