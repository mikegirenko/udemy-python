from treasure_map.treasure_map import *

obj = TreasureMap()


def test_mark_a_spot_2_3():  # 2 is column, 3 is row
    spot_to_mark = "23"
    this_map = obj.mark_a_spot(spot_to_mark)
    obj.print_map(this_map)
    assert obj.mark_a_spot(spot_to_mark)[2][1] == obj.treasure_map[2][1] == "X"


def test_mark_a_spot_1_1():
    spot_to_mark = "11"
    this_map = obj.mark_a_spot(spot_to_mark)
    obj.print_map(this_map)
    assert obj.mark_a_spot(spot_to_mark)[0][0] == obj.treasure_map[0][0] == "X"


def test_mark_a_spot_2_2():
    spot_to_mark = "22"
    this_map = obj.mark_a_spot(spot_to_mark)
    obj.print_map(this_map)
    assert obj.mark_a_spot(spot_to_mark)[1][1] == obj.treasure_map[1][1] == "X"


def test_mark_a_spot_3_1():
    spot_to_mark = "31"
    this_map = obj.mark_a_spot(spot_to_mark)
    obj.print_map(this_map)
    assert obj.mark_a_spot(spot_to_mark)[0][2] == obj.treasure_map[0][2] == "X"
