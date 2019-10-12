import sys

print("Maximum recursion limit: ", sys.getrecursionlimit())


def greet():
    print("hello")
    greet()


# greet()

def fact(n):
    if (n == 0):
        return 1
    return n * fact(n - 1)


print("Factorial of a number using recursion: ", fact(5))

print("__________")

f = lambda a: a * a

print("Square of the number using lambda: ", f(2))
