from classes.mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, rested, is_good=True):
        super().__init__(name,rested)
        self.is_good = is_good

    def __repr__(self):
        return super().__repr__()[:-1] + f", is_good={self.is_good})"
    
    def make_sound(self):
        return "BARKBARKWOOFWOOFARFARF"
    
    def sleep(self):
        super().sleep()
        return f"{self.name} let's out little dream yips."
    
    def run_around(self):
        super().run_around()
        self.is_good = False
        return f"{self.name} is determined to catch that squirrel!"