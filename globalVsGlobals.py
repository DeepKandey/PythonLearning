a = 10


# using global keyword we can use global variable else it will prefer local one and in result, both will have different memory address
def something():
    # a = 18
    global a
    a = 15
    print("Memory address of global a inside function: ", id(a))
    print("in function, value of a using global keyword: ", a)


something()

print("Memory address of global a outside function: ", id(a))
print("outside function, value of global a: ", a)


# using global and local variable in same variable
def somethingGlobal():
    a = 19
    x = globals()['a']
    print("Global value of a:", x)
    print("local value of a: ", a)
    globals()['a'] = 21
    print("Changed value of global a using globals: ", globals()['a'])
    print("Memory address of global a: ", id(a))


somethingGlobal()
print("outside function, value of global a: ", a)

# -------------------------------------------#

print(" --Function which returns multiple values. Print values using format function-- ")


def countOddEven(lst):
    even = 0
    odd = 0

    for i in lst:
        if (i % 2 == 0):
            even += 1
        else:
            odd += 1
    return even, odd


listOfNumbers = [20, 34, 13, 67, 45, 23, 56]
even, odd = countOddEven(listOfNumbers)
print("Even: {} and Odd: {}".format(even, odd))
