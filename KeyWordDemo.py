def person(age, name='Naveen'):
    print(age)
    print(name)


person(name='Deepak', age=56)
person(29)


def add(a, *b):
    c = a
    for i in b:
        c = c + i
    print("sum of the numbers: ", c)


add(4, 5, 67)


def personfunc(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


personfunc('navin', ag=28, city='Mumbai', mob=96531533156)
