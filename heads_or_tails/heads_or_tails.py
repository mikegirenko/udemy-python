"""
program randomly tells user "Heads" or "Tails"
capitalization
randomly generate 1 or 0, then use it to print out "Heads" or "Tails"
"""
import random


class HeadsOrTails:
    def generate_number(self):
        generated_number = random.randint(0, 1)

        return generated_number

    def coin_toss(self):
        coin = ""
        generated_number = self.generate_number()
        if generated_number == 1:
            coin = "Heads"
        if generated_number == 0:
            coin = "Tails"
        if generated_number not in (0, 1):
            raise RuntimeError()

        return coin


if __name__ == "__main__":
    obj = HeadsOrTails()
    print(obj.coin_toss())
