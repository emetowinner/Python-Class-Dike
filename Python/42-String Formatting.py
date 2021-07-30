# How to use the format method to format a string
price = 50
txt = "The price is {} dollars"
print(txt.format(price))

# How to display two decimal place
txt = "The price is {:.2f} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 100
myorder = "I want {} pieces of item numer {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))

# How to use indexing in string formating
quantity = 3
itemno = 567
price = 100
myorder = "I want {1} pieces of item nubmer {2} for {0:.2f} dollars."
print(myorder.format(price,quantity,itemno))

# How to use a named index in string formatting
quantity = 3
itemno = 567
price = 100
myorder = "I want {the_quantity} pieces of item nubmer {the_itemno} for {the_price:.2f} dollars."
print(myorder.format(the_price=price,the_quantity=quantity,the_itemno = itemno))