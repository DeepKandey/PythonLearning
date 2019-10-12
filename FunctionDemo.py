# First implement calling a function by passing variable and check its id or memory address
# INT is immutable, so in case of change a different memory address is assigned

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print(x)


a = 9
print(id(a))
update(a)


# LIST is mutable so memory address does not change
def updatelst(x):
    print(id(x))
    x[0] = 8
    print(id(x))
    print("x", x)


lst = [9, 10, 11]
print(id(lst))
updatelst(lst)
print("lst", lst)
