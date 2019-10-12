class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Inside 1-A class")

    def feature2(self):
        print("Inside 2- A class")


class B:
    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Inside 1-B class")

    def feature4(self):
        print("Inside 2-B class")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("in C init")


c1 = C()
c1.feature1()
