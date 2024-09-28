from data import months

def main():
    while True:
        # User input for date 
        date = input("Date: ")
        # Convert date format into YYYY/MM/DD
        date_formatted = convert(date)
        if date_formatted:
            # Show date in correct format
            print(date_formatted)
            break

def convert(date):
    if date[0].isalpha():
        try: 
            first, year = date.split(",")
            month, day = first.split(" ")
        except ValueError:
            pass
        else: 
            if month in months:
                index = months.index(month)
                month = index + 1
                return f"{year}/{month:02}/{day:02}"
    else:   
        # Split up string into 3 variables
        month, day, year = date.split("/")
        # Return new date with correct format
        return f"{year}/{month: 02}/{day: 02}"

if __name__ == "__main__":
    main()