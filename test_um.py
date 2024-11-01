from um import count

def test_word_before():
    assert count("Hello, um, World") == 1
    assert count("Hello, um, Yummy World") == 1
    assert count("Jesus asdhum") == 0

def test_word_after():
    assert count("Jesus umadhs") == 0