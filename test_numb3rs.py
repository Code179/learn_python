from numb3rs import validate

def test_five_numbers():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.4.5") == False
    assert validate("123.45.67.89.10") == False
    assert validate("123.456.78.90") == False

def test_four_numbers():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.4.5") == False
    assert validate("123.45.67.89.10") == False
    assert validate("123.456.78.90") == False

def test_three_numbers():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.4.5") == False
    assert validate("123.45.67.89.10") == False
    assert validate("123.456.78.90") == False