"""
randomly choose a word, ask user to guess a letter, then check if letter exists in that word
"""
import random


class Hangman:
    def __init__(self):
        self.word_list = ["aardvark", "baboon", "camel"]
        self.chosen_word = random.choice(self.word_list)
        print("Chosen word is", self.chosen_word)

    def play_game(self):
        display = []
        game_over = False
        good_guess = 0
        for i in range(len(self.chosen_word)):
            display.append("_")
        print("Initial display:", display)

        while not game_over:
            guess = input("Guess a letter: ").lower()
            for position in range(len(self.chosen_word)):
                letter = self.chosen_word[position]
                if letter == guess:
                    display[position] = letter
                    good_guess += 1
                    print("Updated display:", display)
                    if good_guess == len(self.chosen_word):
                        game_over = True
                        print("You won!")
                if letter != guess: # TODO do not print if guess was correct
                    print("You wrong")


if __name__ == "__main__":
    obj = Hangman()
    obj.play_game()
