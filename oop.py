import json


class Pet:
    def __init__(self, name):  # This function defines your pet's stats

        self.name = name
        self.hunger = 25
        self.boredom = 25

    def feed(self):
        self.hunger -= 15
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0
        print("You fed (yum)")

    def play(self):
        self.boredom -= 25
        print("yoo its so fun to play with yoohooo")
        if self.boredom > 100:
            self.boredom = 100
        elif self.boredom < 0:
            self.boredom = 0

    def status(self):
        print(f"[Hunger]: {self.hunger}, [Boredom]:  {self.boredom}")

    def save_game(
        self,
    ):
        save_data = {
            "name": self.name,
            "hunger": self.hunger,
            "boredom": self.boredom,
        }

        with open("player_data.json", "w") as file:
            json.dump(save_data, file, indent=4)
            print("Saved. Done.")

    def load_game(self):
        try:
            with open("player_data.json", "r") as file:
                loaded_data = json.load(file)

                self.name = loaded_data["name"]
                self.hunger = loaded_data["hunger"]
                self.boredom = loaded_data["boredom"]

        except FileNotFoundError:
            print("Player data does not exist. Generating...")

            self.save_game()


pet = Pet("YOUR NAME")  # Your pet's name! or your friends oooo


def main():

    pet.load_game()

    game_running = True

    print(f"Look it's your pet {pet.name}! so cute")
    print(
        "Make sure that either stats do not reach 100! otherwise your pet will die and that would suck"
    )

    while pet.hunger < 100 and pet.boredom < 100 and game_running:
        print("Feed, Play, Quit")
        pet.status()
        user_input = input(f"What do you want to do with {pet.name}? :")

        if user_input == "Quit" or user_input == "quit":
            game_running = False
            print("Quitting (Why would you leave your pet?)")
            pet.save_game()  # save

        elif user_input == "Feed" or user_input == "feed":
            pet.feed()

        elif user_input == "Play" or user_input == "play":
            pet.play()
        else:
            print("MISS INPUT (Out of range A-z only)")

    if pet.hunger >= 100 or pet.boredom >= 100:
        print("Your pet died lmao")


main()
