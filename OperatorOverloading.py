class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = m1 + m2
        return m3

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3)

a = 0
print(a)
print(s1)  # overloading __str__ method
