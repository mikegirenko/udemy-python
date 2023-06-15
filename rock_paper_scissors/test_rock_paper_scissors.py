from rock_paper_scissors.rock_paper_scissors import *

obj = RockPaperScissors()


def test_game():
    assert obj.game(0, 0) == "Draw"
    assert obj.game(2, 2) == "Draw"
    assert obj.game(0, 2) == "User wins"
    assert obj.game(2, 0) == "Computer wins"
    assert obj.game(2, 1) == "User wins"
    assert obj.game(1, 0) == "User wins"
    assert obj.game(1, 2) == "Computer wins"
    assert obj.game(0, 1) == "Computer wins"
