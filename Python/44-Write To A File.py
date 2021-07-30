# How to write to a file using the open method

# How to write to a file using the append mode
f = open("demofile.txt","a")
f.write("Now the file has more content!!")
f.close()

f = open("demofile.txt","w")
f.write("Woops! I have deleted the contents!")
f.close()

# How to create a file using the open method
# y = open("test3.txt","x")

# Trying to create other extension files
# y = open("test3.csv","x")
y = open("test3.xlsx","x")