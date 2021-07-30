# How to open a file using the open method
f = open("demofile.txt")

# How to open a file in read mode

f = open("demofile.txt","r")
# print(f.read(20))

# How to read a full line in your text
f = open("demofile.txt","r")
# print(f.readline())

# How to loop through your file
for data in f:
    print(data)

f.close()
