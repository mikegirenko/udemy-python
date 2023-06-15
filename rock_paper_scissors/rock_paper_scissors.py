"""
Make a rock, paper, scissors game.
Take player input, randomly generate choice for the computer, compare them, and determine winner.
Game logic - draw, a win, or a loss
Scissors beats paper, paper beats rock, rock beats scissors
Give player feedback
"""
import random


class RockPaperScissors:
    def get_user_input(self) -> str:
        user_input = input(
            "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "
        )
        if user_input not in ["0", "1", "2"]:
            raise RuntimeError("Please enter 0, 1, or 2")

        return int(user_input)

    def get_computer_choice(self) -> int:
        return random.randint(0, 2)

    def human_readable_computer_choice(self, computer_choice_as_integer) -> str:
        human_readable_computer_choice = ""
        if computer_choice_as_integer == 0:
            human_readable_computer_choice = "Rock"
        if computer_choice_as_integer == 1:
            human_readable_computer_choice = "Paper"
        if computer_choice_as_integer == 2:
            human_readable_computer_choice = "Scissors"

        return human_readable_computer_choice

    def game(self, user_input, computer_choice) -> str:
        game_result = ""
        if user_input == computer_choice:  # draw
            game_result = "Draw"
        elif user_input == 0 and computer_choice == 2:  # rock(0) beats scissors(2)
            game_result = "User wins"
        elif user_input == 2 and computer_choice == 0:  # rock(0) beats scissors(2)
            game_result = "Computer wins"
        elif (
            user_input > computer_choice
        ):  # scissors(2) beats paper(1), paper(1) beats rock(0)
            game_result = "User wins"
        elif (
            user_input < computer_choice
        ):  # scissors(2) beats paper(1), paper(1) beats rock(0)
            game_result = "Computer wins"

        return game_result


if __name__ == "__main__":
    obj = RockPaperScissors()
    user_input = obj.get_user_input()
    computer_choice = obj.get_computer_choice()
    human_readable_computer_choice = obj.human_readable_computer_choice(computer_choice)
    print("Computer choice is", human_readable_computer_choice)
    play_game = obj.game(user_input, computer_choice)
    print(play_game)
