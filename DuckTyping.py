class Pycharm:

    def execute(self):
        print("Compling")


class MyEditor:
    def execute(self):
        print("Compling")
        print("Spell Check")


class Laptop:
    def __init__(self, ide):
        ide.execute()


# ide = Pycharm()
ide = MyEditor()

L1 = Laptop(ide)
