from bmi.bmi import Bmi

obj = Bmi()


def test_calculate_bmi():
    assert obj.calculate_bmi(1.8, 59) == 18
    assert obj.calculate_bmi(1.75, 67) == 22
    assert obj.calculate_bmi(1.75, 85) == 28
    assert obj.calculate_bmi(1.75, 100) == 33
    assert obj.calculate_bmi(1.75, 122) == 40
