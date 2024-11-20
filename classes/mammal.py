class Mammal:

    def __init__(self, name, rested):
        self.name = name
        self.rested = rested

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, rested={self.rested})"

    def make_sound(self):
        return "generic mammal sound"

    def sleep(self):
        self.rested = True

    def run_around(self):
        self.rested = False