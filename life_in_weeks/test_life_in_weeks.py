import pytest

from life_in_weeks.life_in_weeks import calculate_days_left


def test_calculate():
    assert calculate_days_left() == 14600
