from treasure_map.treasure_map import *

obj = TreasureMap()


def test_mark_a_spot_2_3():
    spot_to_mark = "23"
    assert obj.mark_a_spot(spot_to_mark)[2][1] == obj.treasure_map[2][1] == "x"


def test_mark_a_spot_0_0(): # TODO fails
    spot_to_mark = "00"
    assert obj.mark_a_spot(spot_to_mark)[0][0] == obj.treasure_map[0][0] == "x"


def test_print_map():
    spot_to_mark = "23"
    this_map = obj.mark_a_spot(spot_to_mark)
    obj.print_map(this_map)
