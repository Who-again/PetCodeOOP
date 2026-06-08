class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.boredom = 50

    def feed(self):
        self.hunger -= 15
        print("You fed (yum)")

    def play(self):
        self.boredom -= 25
        print("yoo its so fun to play with yoohooo")

    def status(self):
        print(f"Hunger: {self.hunger}, Boredom:  {self.boredom}")


pet = Pet("Kitten")

print(pet.name)
# it feels weird as hell trying OOP after a 11 days of straight procedural programming
