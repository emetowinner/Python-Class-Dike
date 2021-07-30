#Python Built-in Data Types

"""
Text Type: str
Numeric Types: int, float, complex
Mapping Type: dict
Sequence Types: list,tuple,range
Set Type: set
Boolean Type: bool

"""

x = 5
print(type(x))


# String Type
x = "Hello World" 
x = str("Hello World")

# Int Type
x = 20
x = int(20)

#Float Type
x = 20.5
x = float(20.5)

#Complex Type
x = 1j
x = complex(1j)
#List Type
x = ["apple","banana","cherry"]
x = list(("apple","banana","cherry"))

#Tuple Type
x = ("apple","banana","cherry")
x = tuple(("apple","banana","cherry"))

#Range Type
x = range(6)

#Dict Type
x = {"name":"Winner","age":30}
x = dict(name="Winner",age=30)

#Set Type
x = {"apple","banana","cherry"}
x = set(("apple","banana","cherry"))

#Boolean Type
x = True
x = False
x = bool(5)

#Evaluation to boolean value
x = "" #This will evaluate to a boolean value of False
x = 0 #This will evaluate to a boolean value of False
x = [] #This will evaluate to a boolean value of False
x = () #This will evaluate to a boolean value of False
x = {} #This will evaluate to a boolean value of False

#NOTE: Every other thing evaluates to True