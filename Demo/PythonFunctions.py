
def printHello():
    print("Hello")

printHello()

def printHi(name="John"):
    print("Hi, " + name)

printHi("Daphne")
printHi()

def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)

def returnSum(a,b):
    """"this is a function to calculate sum of two numbers"""
    return (a+b)

x = returnSum(10,20)
print(x)