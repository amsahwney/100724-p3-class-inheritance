from classes.mammal import Mammal

class Cat( Mammal ):

    def __init__(self, name, rested = True, lives_remaining=9):
        super().__init__(name,rested)
        self.lives_remaining = lives_remaining
    
    def __repr__(self):
        # return f"Cat(name={self.name}, rested={self.rested})"
        return super().__repr__()[:-1] + f", lives_remaining={self.lives_remaining})"
    
    def make_sound(self):
        return "MEOWMEOWMEOW"
    
    def sleep(self):
        super().sleep()
        return f"{self.name}'s little paws are running in their dreams"
