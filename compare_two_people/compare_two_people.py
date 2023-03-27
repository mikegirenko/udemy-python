class LoveScore:
    def accept_user_input(self) -> tuple:
        print("Welcome to the Love Calculator!")
        first_name = input("What is your name, first person? ")
        second_name = input("What is your name, second person? ")

        return first_name, second_name

    def calculate_love_score(self, name_one, name_two) -> str:
        true_counter = self.count_letters_using_count(name_one, name_two, "TRUE")
        love_counter = self.count_letters_using_count(name_one, name_two, "LOVE")

        two_digits_number = f"{true_counter}{love_counter}"

        return two_digits_number

    # def count_letters(self, name_one, name_two, word_to_use) -> int:
    #     letter_counter = 0
    #     names_to_check = name_one + name_two
    #     for letter in word_to_use.lower():
    #         if letter in names_to_check:
    #             letter_counter += 1
    #     return letter_counter

    def count_letters_using_count(self, name_one, name_two, word_to_use) -> int:
        letter_counter = 0
        names_to_check = name_one.lower() + name_two.lower()
        for letter in word_to_use.lower():
            letter_counter = letter_counter + names_to_check.count(letter)

        return letter_counter

    def print_output(self, love_score):
        score_to_check = int(love_score)
        if score_to_check < 10 or score_to_check > 90:
            print(f"Your score is {love_score}, you go together like coke and mentos.")
        elif 40 < score_to_check < 50:
            print(f"Your score is {love_score}, you are alright together.")
        else:
            print(f"Your score is {love_score}.")


if __name__ == "__main__":
    obj = LoveScore()
    first_name, second_name = obj.accept_user_input()
    love_score = obj.calculate_love_score(first_name, second_name)
    obj.print_output(love_score)
