from leap_year.leap_year import LeapYear

obj = LeapYear()


def test_leap_year_or_not():
    assert obj.leap_year_or_not(2000)
    assert obj.leap_year_or_not(2400)
    assert not obj.leap_year_or_not(2100)
    assert not obj.leap_year_or_not(1989)


def test_print_output_true():
    obj.print_output(True)


def test_print_output_false():
    obj.print_output(False)
