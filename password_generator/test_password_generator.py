from password_generator.password_generator import *

obj = PasswordGenerator()


def test_generate_letters():
    assert len(obj.generate_letters(3)) == 3


def test_generate_symbols():
    assert len(obj.generate_symbols(3)) == 3


def test_generate_numbers():
    assert len(obj.generate_numbers(3)) == 3


def test_generate_easy_level_password():
    letters = ["a", "b"]
    symbols = ["&", "*"]
    numbers = ["2", "4"]
    assert obj.generate_easy_level_password(letters, symbols, numbers) == [
        "a",
        "b",
        "&",
        "*",
        "2",
        "4",
    ]


def test_generate_hard_level_password():
    letters = ["a", "b"]
    symbols = ["&", "*"]
    numbers = ["2", "4"]
    assert obj.generate_hard_level_password(letters, symbols, numbers) == 0
