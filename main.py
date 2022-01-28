class Calculator:
    def __init__(self):
        self.result = 0
    def lumSum(self, a):
        self.result += a
        return self.result


acompany = Calculator()
a = 0
while True:
     a += 1
     acompany.lumSum(a)
     if(a == 10):
           break

print(acompany.result)

