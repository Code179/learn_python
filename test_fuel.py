from fuel import gauge, convert

def test_convert():
    assert convert("3/4") == 75
    assert convert("a/a") == None
    assert convert("4/2") == None

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"