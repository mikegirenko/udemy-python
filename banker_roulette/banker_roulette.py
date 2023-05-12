"""
Program selects a random name from list of names
The selected name will pay the food bill
"""
import random

NAMES_STRING = "Angela, Ben, Jenny, Michael, Chloe"


class BankerRoulette:
    def select_name(self, string_of_names: str):
        list_of_names = string_of_names.split(", ")
        randomizer = random.randint(0, len(list_of_names) - 1)
        name = list_of_names[randomizer]

        return name


if __name__ == "__main__":
    obj = BankerRoulette()
    person_paying = obj.select_name(NAMES_STRING)
    print(f"{person_paying} is going to pay the meal today!")
