def main():
    text = input("Enter text: ")
    short_text = shorten(text)
    print(short_text)

def shorten(text):
    short_text = ""
    for t in text:
        if t.lower() not in ["a", "e", "i", "o", "u"]:
            short_text += short_text.join(t)
    return short_text
if __name__ == "__main__":
    main()