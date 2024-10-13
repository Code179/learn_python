def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(amount)

def value(greeting):
    greeting = greeting.lower()
    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()