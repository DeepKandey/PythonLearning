import math

# Example for forElse where loop ends without break
nums = [23, 56, 39, 19, 41]
for num in nums:
    if num % 5 == 0:
        break
else:
    print("not found in the given list")

num = int(input("Enter number to check its prime or not "))
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        print(num, "Not a prime number")
        break;
else:
    print(num, "Prime number")
