class Computer:
    computer_company = "Dell"

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)


x = 9
print("Type of 9:", type(x))

a = 'Deepak'
print("Type of Deepak: ", type(a))

com1 = Computer('i5', 16)
com2 = Computer('i7', 16)

print("Type of object com1: ", type(com1))
Computer.config(com1)  # Calling config for com1 using Class name
com1.ram = 32  # changing ram value
com1.config()  # Calling config for com1 using object name
print("Memory address of object com1: ", id(com1))
print("Computer company name for com1: ", com1.computer_company)
com1.computer_company = "Toshiba"
print("Computer company name: ", com1.computer_company)
print("Computer company name for com2: ", com2.computer_company)
