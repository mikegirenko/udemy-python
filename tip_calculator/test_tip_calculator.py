from tip_calculator.tip_calculator import calculate_tip


def test_calculate_tip():
    bill = 150
    number_of_people = 5
    tip_in_percents = 12

    assert calculate_tip(bill, number_of_people, tip_in_percents) == "33.60"
