from average_height.average_height import *

obj = AverageHeight()


def test_calculate_average_height():
    list_to_calculate = [100, 100, 100]
    assert obj.calculate_average_height(list_to_calculate) == 100
    list_to_calculate = [168]
    assert obj.calculate_average_height(list_to_calculate) == 168
    list_to_calculate = [180, 124, 165, 173, 189, 169, 146]
    assert obj.calculate_average_height(list_to_calculate) == 164
    list_to_calculate = [156, 178, 165, 171, 187]
    assert obj.calculate_average_height(list_to_calculate) == 171
