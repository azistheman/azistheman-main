import random

class Character:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def attack(self):
        # Generate a random attack power based on the character's power level
        return random.uniform(0.5, 1.5) * self.power_level

    def __str__(self):
        return f"{self.name} (Power Level: {self.power_level})"

def battle(character1, character2):
    print(f"Battle begins between {character1} and {character2}!")

    # Simulate battle
    while True:
        attack1 = character1.attack()
        attack2 = character2.attack()

        print(f"{character1.name} attacks with power: {attack1:.2f}")
        print(f"{character2.name} attacks with power: {attack2:.2f}")

        # Determine the winner
        if attack1 > attack2:
            print(f"{character1.name} wins the battle!")
            break
        elif attack2 > attack1:
            print(f"{character2.name} wins the battle!")
            break
        else:
            print("It's a tie! Both characters are evenly matched. Trying again...\n")

# Create Goku and Saitama with arbitrary power levels
goku = Character(name="Goku", power_level=1000000)
saitama = Character(name="Saitama", power_level=100000)  # Saitama is overpowered for this example

# Simulate the battle
battle(goku, saitama)
