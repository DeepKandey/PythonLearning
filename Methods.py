class MethodsTypes:
    school = 'Telusko'

    def avegrage(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def getSchoolName(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class...in abc module")


s1 = MethodsTypes(23, 45, 67)
s1 = MethodsTypes(231, 45, 67)

print(s1.avegrage())
print(MethodsTypes.getSchoolName())
MethodsTypes.info()
