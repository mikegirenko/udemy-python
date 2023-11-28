"""
randomly choose a word, ask user to guess a letter, then check if letter exists in that word
"""
import random


class Hangman:
    def __init__(self):
        self.word_list = ["aardvark", "baboon", "camel"]
        self.chosen_word = random.choice(self.word_list)
        print("Chosen word is", self.chosen_word)
        self.guess = input("Guess a letter: ").lower()

    def play_game(self):
        display = []
        for i in range(len(self.chosen_word)):
            display.append("_")
        print("Initial display", display)

        for position in range(len(self.chosen_word)):
            letter = self.chosen_word[position]
            if letter == self.guess:
                display[position] = letter
            else:
                print("Wrong")

        print("Updated display", display)


if __name__ == "__main__":
    obj = Hangman()
    obj.play_game()
