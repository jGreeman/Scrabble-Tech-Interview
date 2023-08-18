from solution import calculate_score, seven_random_tiles

def test_guardian():
    assert calculate_score("GUARDIAN") == 10


def test_length_changes():
    letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    start_len = len(letter_list)
    tiles = seven_random_tiles(letter_list)
    fin_len = len(letter_list)
    assert start_len != fin_len


def test_rack_length_seven():
    letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    rack = seven_random_tiles(letter_list)
    assert len(rack) == 7