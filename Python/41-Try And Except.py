""""

So most times you will definetly know that you code will return an error, especialy when the data input is 
dependent on the user of the program, in this case, you need a way to counter those errors known as exceptions in 
your code or program

"""
# print(x)
try:
    print(x)
except:
    print("An exception occured")

print("My code is still running")

# Capturing errors
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else occured")

try:
    x = 4
    y = "5"
    print(x/y)
except TypeError:
    print("unsupported operand type(s) for /: 'int' and 'str'")
    print("Please make sure your variables are of the same type")
    print("x is of the type ",type(x)," and your y is of the type ",type(y))

# How to define your own error or raise your own error
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero!")