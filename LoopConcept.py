# break example
availableCandies = 5
x = int(input("How many candies you want"))
i = 1
while i <= x:
    if i > availableCandies:
        print("Out of stock")
        break
    print("Candy")
    i += 1
print("Bye")

# continue example
for j in range(1, 10):
    if j % 3 == 0:
        continue
    print(j)
print("End of for loop")

# pass example
for j in range(1, 10):
    if j % 3 != 0:
        pass
    else:
        print(j)
print("End of for loop")
