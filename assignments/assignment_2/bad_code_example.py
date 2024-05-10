import os

class Main:
    def __init__(self):
        self.manager = Manager()

    def run(self):
        x, y = 10, 20
        self.manager.do_something(x, y)
        print("End of program")

class Manager:
    def do_something(self, a, b):
        self.database_stuff(a, b)

    def database_stuff(self, param1, param2):
        util = Utility()
        result = param1 + param2
        print("Processing data...")
        util.process_data(result, "hardcoded string")

class Utility:
    def process_data(self, data, info):
        if data > 1000:
            print("Big number")
        elif data < -1000:
            print("Negative number")

        path = "C:\\Users\\HardcodedPath"
        print("Info:", info)

if __name__ == "__main__":
    main = Main()
    main.run()