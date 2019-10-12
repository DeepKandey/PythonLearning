from functools import reduce


# filter function example
def isEven(n):
    return n % 2 == 0


def add_all(a, b):
    return a + b


num = [23, 56, 12, 57, 56, 76]

evens = list(filter(isEven, num))
odds = list(filter(lambda n: n % 2 != 0, num))  # using lambda
doubles = list(map(lambda n: n * 2, evens))  # using Map and lambda
sum = reduce(lambda a, b: a + b, doubles) #using sum 
print("Even numbers: ", evens)
print("Odd numbers: ", odds)
print("Doubles for the even numbers: ", doubles)
print("Sum of all doubles: ", sum)
