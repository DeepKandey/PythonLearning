f = open("Data", 'r')

# print(f.read())
print(f.readline())

f1 = open("abc", 'a')
f1.write("I am good")

for data in f:
    f1.write(data)
