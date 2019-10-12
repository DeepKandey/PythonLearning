from numpy import *

# Numpy example
arr = array([1, 6, 4, 7])
print(arr)
print(arr.dtype)

arr = linspace(0, 16, 13)
print(arr)

arr = arange(0, 12, 2)
print(arr)

arr = ones(5, int)
print(arr)

arr = zeros(5, int)
print(arr)

arr= arr+5
print(arr)

print(sin(arr))

arr1= array([3,4565,21])
arr= array([6,8,3,2])
print(concatenate([arr,arr1]))

#copying array
arr2= array([4,5])
arr3= arr2

print(arr3)
print(id(arr3))
print(id(arr2))

arr4= array([8,5])
arr5= arr4.view() # shallow copy

arr4[0]=9
print(arr4)
print(arr5)
print(id(arr4))
print(id(arr5))

arr5= arr4.copy() #  deep copy

arr4[0]=10
print(arr4)
print(arr5)
print(id(arr4))
print(id(arr5))

#multi dimensional
multarray = array([
    [1,2,3,6,3,4],
    [5,6,7,6,4,1]
])
print(multarray)
print(multarray.ndim)
print(multarray.shape)
print(multarray.size)
single= multarray.flatten()
print(single)

threedimension= single.reshape(3,4)
print(threedimension)