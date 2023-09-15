import random

"""
A program to generate password
"""


class PasswordGenerator:
    def __init__(self):
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.symbols = ["!", "#", "$", "%", "&", "*", "+"]

    def user_input(self):
        print("Welcome to the Password Generator! ")
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))

        return nr_letters, nr_symbols, nr_numbers

    def generate_letters(self, letters_count) -> list:
        letters = []
        for i in range(0, letters_count):
            random_index = random.randint(0, letters_count)
            letters.append(self.letters[random_index - 1])

        return letters

    def generate_symbols(self, symbols_count) -> list:
        symbols = []
        for i in range(0, symbols_count):
            random_index = random.randint(0, symbols_count)
            symbols.append(self.symbols[random_index - 1])

        return symbols

    def generate_numbers(self, numbers_count) -> list:
        numbers = []
        for i in range(0, numbers_count):
            random_index = random.randint(0, numbers_count)
            numbers.append(self.numbers[random_index - 1])

        return numbers

    def generate_easy_level_password(self, letters, symbols, numbers) -> str:
        password = letters + symbols + numbers

        return password

    def generate_hard_level_password(self, letters, symbols, numbers):
        hard_level_password_list = (
            letters + symbols + numbers
        )  # need to have same length as input
        easy_level_password = letters + symbols + numbers
        indexes_list = []  # this it randomly generated indexes
        for i in range(0, len(easy_level_password)):
            random_index = random.randint(0, len(easy_level_password) - 1)
            indexes_list.append(random_index)
        for ch in easy_level_password:
            i = 0
            hard_level_password_list[indexes_list[i]] = ch
            i += 1

        password_string = "".join(str(ch) for ch in hard_level_password_list)

        return password_string


if __name__ == "__main__":
    obj = PasswordGenerator()
    letters, symbols, numbers = obj.user_input()

    easy_level_password = obj.generate_easy_level_password(
        obj.generate_letters(letters),
        obj.generate_symbols(symbols),
        obj.generate_numbers(numbers),
    )
    print(f"Your easy level password is {easy_level_password}")

    hard_level_password = obj.generate_hard_level_password(
        obj.generate_letters(letters),
        obj.generate_symbols(symbols),
        obj.generate_numbers(numbers),
    )
    print(f"Your hard level password is {hard_level_password}")
