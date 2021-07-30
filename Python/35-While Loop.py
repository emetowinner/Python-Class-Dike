# With the while loop we can execute a set of statement as long as a condition is true

# Eg: print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

# How to use the break statement
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# How to use the continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)    