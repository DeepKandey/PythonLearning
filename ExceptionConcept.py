a = 5
b = 0

try:
    print(a / b)
except Exception as e:
    print("you can not divide any number by zero ", e)
finally:
    print("Resource Closed")
