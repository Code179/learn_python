from plates import is_valid

def test_two_letters():
    assert is_valid("22") == False
    assert is_valid("AA") == True

def test_min_max_char():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAA22") == True

def test_no_number_in_middle():
    assert is_valid("AA22DD") == False
    assert is_valid("AA2D") == False
    assert is_valid("AADD2") == True

def test_first_number_not_zero():
    assert is_valid("0AAAAA") == False
    assert is_valid("AA00SS") == False
    assert is_valid("A0") == False

def test_no_pun_space_period():
    assert is_valid("AA 22") == False
    assert is_valid("AA.A22") == False
    assert is_valid("AA,AA") == False