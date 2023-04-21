from unittest.mock import patch

from heads_or_tails.heads_or_tails import HeadsOrTails

obj = HeadsOrTails()


def test_coin_toss():
    assert obj.coin_toss() in ["Heads", "Tails"]


@patch("heads_or_tails.heads_or_tails.HeadsOrTails.generate_number")
def test_coin_toss_using_mock(mocked_generated_number):
    mocked_generated_number.return_value = 0
    assert obj.coin_toss() == "Tails"
