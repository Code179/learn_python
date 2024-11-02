from datetime import date
import inflect
import sys

def main():
    try:
        birthday = date.fromisoformat(input("Enter your birthday in YYYY-MM-DD format: "))
        age_in_minutes = calculate_minutes(birthday)
    except ValueError:
        sys.exit("Invalid Date")
    engine = inflect.engine()
    print(f"{engine.number_to_words(age_in_minutes, andword="").capitalize()} minutes")

def calculate_minutes(birthday):
    timedelt = (date.today() - birthday).total_seconds() / 60
    return round(timedelt)

if __name__ == "__main__":
    main()
