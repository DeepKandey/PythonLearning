class InnerClass:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


class Mobile(InnerClass):  # Inheritance

    def __init__(self):
        super(Mobile, self).__init__('Pankaj', 234)
        print("in B init")


M1 = Mobile()
M1.show()
s1 = InnerClass('Deepak', 100)
s1.show()
l1 = InnerClass.Laptop()
