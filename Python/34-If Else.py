# Python supports the usual logical conditions from maths
"""

Equals: q == b
Not Equals:  a != b
Less Than:  a < b
Less Than Or Equal To:  a <= b
Greater Than:  a > b
Greater Than Or Equals To:  a >= b

"""
a = 33
b = 200

# How to use the if statement
if b > a:
    print("b is greater than a")

# Trying this in a wrong way
# if b > a:
# print("B is greater tha A") # You will get an error!

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Using logic operators
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")

if a > b or b > c:
    print("One of the conditions were true")