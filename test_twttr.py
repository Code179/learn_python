from twttr import shorten

import pytest


def test_upper():
  assert shorten("WHAT IS THIS") == "WHT S THS"
  assert shorten("LOL") == "LL"

def test_lower():
  assert shorten("what is this") == "wht s ths"
  assert shorten("lol") == "ll"


def test_upper_lower():
  assert shorten("What is this") == "Wht s ths"


def test_number():
  # Expect an exception of a TypeError whenever the input is a string like "cat"
  with pytest.raises(TypeError):
    shorten(5)
