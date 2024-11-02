from seasons import calculate_minutes
from datetime import date

def test_minutes():
    assert calculate_minutes(date(1997, 7, 29)) == 14339520