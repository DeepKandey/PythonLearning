# Pattern1
for i in range(4):
    for j in range(4):
        print(" # ", end="")
    print()

print("---------")

# Pattern2
for k in range(4):
    for l in range(k+1):
        print(" # ", end="")
    print()

print("---------")

# Pattern3
for k in range(4):
    for l in range(4-k):
        print(" # ", end="")
    print()
