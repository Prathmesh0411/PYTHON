class Animals:
    def __init__(self):
        pass
    
class Pets(Animals):
    def __init__(self):
        pass
    
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")
        
d = Dog()
d.bark()