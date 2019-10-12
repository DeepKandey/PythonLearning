from array import *
from numpy import  *

vals = array('i', [5, 9, 3, 2])
print(vals)  # priny array values
print(vals.buffer_info(), "Buffer Info of the array")  # print memory allocation and size using tuple
print(vals.typecode, "Type code of the array")  # array type
print(vals[0], "Values at index 0")  # print array using index

# print array using for loop
print("---Print array values using For loop---")
for i in range(len(vals)):
    print(vals[i], end=" ")
print()

# print reverse array
print("---Reverse the loop and print it---")
vals.reverse()
print(vals)

# Advanced for loop
print("---Print array values using advanced For loop---")
for e in vals:
    print(e, end=" ")
print()

# copying array
print("---Copy the array and then print square of it---")
newArr = array(vals.typecode, (a * a for a in vals))
for e in newArr:
    print(e, end=" ")
print()

#
print("---Take input from user and then print the array---")
arr = array('i', [])  # blank array
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)
# Print the index of the number you want to search in array
searchNumber = int(input("Enter the number you want to search"))

k = 0
for e in arr:
    if e == searchNumber:
        print(k)
        break
    k += 1
else:
    print("not found in the given list")
# Using in built function
print(arr.index(searchNumber))