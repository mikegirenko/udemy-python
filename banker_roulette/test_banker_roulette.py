from banker_roulette.banker_roulette import *

obj = BankerRoulette()


def test_select_name():
    assert obj.select_name(NAMES_STRING) in NAMES_STRING
