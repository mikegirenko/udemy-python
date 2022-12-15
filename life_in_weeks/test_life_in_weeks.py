from life_in_weeks.life_in_weeks import calculate_days_left, calculate_weeks_left, \
    calculate_months_left


def test_calculate_days_left():
    assert calculate_days_left(50) == 14600


def test_calculate_weeks_left():
    assert calculate_weeks_left(50) == 2240


def test_calculate_months_left():
    assert calculate_months_left(50) == 480
