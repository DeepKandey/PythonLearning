class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def show(self):
        print("in Student show")

    def sum(self, a=None, b=None, c=None):
        s = 0

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(2, 6)

print(s1.sum(5))
print(s1.sum(5, 6))
print(s1.sum(5, 9, 14))


class Student_A(Student):

    def __init__(self):
        pass

    def show(self):
        print("in Student_A show")


s2 = Student(2, 6)
s2.show()

# Method overriding
s3 = Student_A()
s3.show()
