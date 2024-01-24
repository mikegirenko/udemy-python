"""
randomly choose a word, ask user to guess a letter, then check if letter exists in that word.
print ASCII art based on number of lives remaining
"""
import random
from hangman_words import word_list
from hangman_art import logo, stages


class Hangman:
    def __init__(self):
        self.word_list = word_list
        self.chosen_word = random.choice(self.word_list)
        self.lives = 6
        print("Chosen word is", self.chosen_word)

    def play_game(self):
        display = []
        game_over = False
        good_guess = 0
        for i in range(len(self.chosen_word)):
            display.append("_")
        print(logo)
        print("Initial display:", display)
        while not game_over:
            guess = input("Guess a letter: ").lower()
            if guess in display:  # this letter was already guessed
                print(f"You already guessed this letter '{guess}'")
            if guess in self.chosen_word:  # guess is correct
                list_of_indexes = [
                    pos for pos, char in enumerate(self.chosen_word) if char == guess
                ]
                for index in list_of_indexes:
                    display[index] = guess
                    good_guess += 1
                if good_guess == len(self.chosen_word):
                    game_over = True
                    print("You won!")
            if guess not in self.chosen_word:  # guess is not correct
                self.lives -= 1
                print(f"Letter '{guess}' is not in the word")
            if self.lives == 0:
                game_over = True
                print("You lose!")
            print("Updated display:", display)
            print(stages[self.lives])  # print ASCII art


if __name__ == "__main__":
    obj = Hangman()
    obj.play_game()
