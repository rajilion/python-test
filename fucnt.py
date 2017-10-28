class calculator:
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(a,b):
        return a / b
if __name__ == '__main__':
    num1 = eval(input('first number'))
    num2 = eval(input('second number'))
    a = calculator
    print (a.add(num1,num2))

