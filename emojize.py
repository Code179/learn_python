import emoji
def main():
    # Ask user for input
    user_input = input("Input: ")
    # Print user input in emojis
    print(emoji.emojize(user_input, language='de'))

if __name__ == "__main__":
    main()