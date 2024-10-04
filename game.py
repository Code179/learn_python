import random

def main():
    number = 0
    random_number = 0
    guess = 0

    while int(number) <= 0:
        number = input("Enter a number: ")
    random_number = random.randint(1, int(number))
    print(random_number)
    while int(guess) <= 0:
        while int(guess) != random_number:
            guess = input(f"Guess a number between 1 and {number}: ")
            guess = int(guess)

            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            elif guess == random_number:
                print("Congratulations!")
                break

if __name__ == "__main__":
    main()