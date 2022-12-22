from odd_or_even.odd_or_even import OddOrEven


def test_odd_or_even():
    obj = OddOrEven()
    assert obj.determine_odd_or_even(86) == "even number"
    assert obj.determine_odd_or_even(59) == "odd number"
