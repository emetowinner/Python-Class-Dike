# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function
# A function return data as result.

# In python a function is defined using the def keyword
def my_function():
    print("Hello from a function")

my_function()

# Functions with arguments
def my_function_1(xyz):
    print("Function " + str(xyz))

my_function_1("Winner")
my_function_1("Emeto")
my_function_1(10)

# Function with more than one parameter
def add_nums(num1,num2):
    print(num1+num2)

add_nums(14,20)

# Arbitrary Arguments
def my_function_2(*kids):
    # print("The first item in the list is " , kids[1])
    counter = 0
    for item in kids:
        print(item)
        if counter == 2:
            break
        counter += 1

my_function_2("Emil","Tobias","Winner","John")

# Aerbitrary Keyword Arguments, **kwargs
def my_function_3(**kids):
    print(kids)

my_function_3(name1="Winner",name2="Emeto",name3="John")

# Default parameter
def my_function_4(name="Winner Emeto"):
    print(name)

my_function_4("John Mike")
my_function_4()

# Passing a list to a function
x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
def my_function_5(food):
    for item in food:
        print(item)

my_function_5(x)

# How to write a function that return a value
def sum_nums(num1,num2):
    result = num1 + num2
    return result

result = sum_nums(30,10)
division = 500/result
print(division)