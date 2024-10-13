from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0
def test_h():
    assert value("h") == 20
    assert value("H") == 20
    assert value("hase") == 20
    assert value("hell") == 20
def test_wrong():
    assert value("jesus") == 100
    assert value("j") == 100