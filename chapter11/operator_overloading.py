class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n
    
n = Number(8)
m = Number(7)

print(n + m)