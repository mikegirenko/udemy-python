from compare_two_people.compare_two_people import *

obj = LoveScore()


def test_count_letters_angela_jack_true():
    name_one = "Angela Yu"
    name_two = "Jack Bauer"
    word_to_check = "TRUE"
    assert obj.count_letters_using_count(name_one, name_two, word_to_check) == 5


def test_count_letters_angela_jack_love():
    name_one = "Angela Yu"
    name_two = "Jack Bauer"
    word_to_check = "LOVE"
    assert obj.count_letters_using_count(name_one, name_two, word_to_check) == 3


def test_count_letters_kanye_kim_true():
    name_one = "Kanye West"
    name_two = "Kim Kardashian"
    word_to_check = "TRUE"
    assert obj.count_letters_using_count(name_one, name_two, word_to_check) == 4


def test_count_letters_kanye_kim_love():
    name_one = "Kanye West"
    name_two = "Kim Kardashian"
    word_to_check = "LOVE"
    assert obj.count_letters_using_count(name_one, name_two, word_to_check) == 2


def test_count_letters_john_yoko_true():
    name_one = "John Lennon"
    name_two = "Yoko Ono"
    word_to_check = "TRUE"
    assert obj.count_letters_using_count(name_one, name_two, word_to_check) == 1


def test_count_letters_john_yoko_love():
    name_one = "John Lennon"
    name_two = "Yoko Ono"
    word_to_check = "LOVE"
    assert obj.count_letters_using_count(name_one, name_two, word_to_check) == 8


def test_calculate_love_score_catherine_michael():
    name_one = "Catherine Zeta-Jones"
    name_two = "Michael Douglas"
    assert obj.calculate_love_score(name_one, name_two) == "99"


def test_calculate_love_score_brad_jennifer():
    name_one = "Brad Pitt"
    name_two = "Jennifer Aniston"
    assert obj.calculate_love_score(name_one, name_two) == "73"


def test_calculate_love_score_prince_kate():
    name_one = "Prince William"
    name_two = "Kate Middleton"
    assert obj.calculate_love_score(name_one, name_two) == "67"


def test_calculate_love_score_anjela_jack():
    name_one = "Angela Yu"
    name_two = "Jack Bauer"
    assert obj.calculate_love_score(name_one, name_two) == "53"


def test_calculate_love_score_kanye_kim():
    name_one = "Kanye West"
    name_two = "Kim Kardashian"
    assert obj.calculate_love_score(name_one, name_two) == "42"


def test_calculate_love_score_beyonce_jay():
    name_one = "Beyonce"
    name_two = "Jay-Z"
    assert obj.calculate_love_score(name_one, name_two) == "23"


def test_calculate_love_score_beyonce_jay():
    name_one = "Beyonce"
    name_two = "Jay-Z"
    assert obj.calculate_love_score(name_one, name_two) == "23"


def test_calculate_love_score_john_yoko():
    name_one = "John Lennon"
    name_two = "Yoko Ono"
    assert obj.calculate_love_score(name_one, name_two) == "18"
