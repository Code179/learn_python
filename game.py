import random

def main():
    max_number = get_positive_integer("Enter a positive number: ")
    random_number = random.randint(1, max_number)

    guess = 0
    while guess != random_number:
        guess = get_positive_integer(f"Guess a number between 1 and {max_number}: ")
        
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Congratulations!")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()