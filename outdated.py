from data import months

def main():
    # User input for date 
    date = input("Date: ")
    # Convert date format into YYYY/MM/DD
    date_formatted = convert(date)
    # Show date in correct format
    print(date_formatted)

def convert(date):
    if date[0].isalpha():
        first, year = date.split(",")
        month, day = first.split(" ")
        if month in months:
            index = months.index(month)
            month = index + 1
            return f"{year}/{month}/{day}"
    else:   
        # Split up string into 3 variables
        month, day, year = date.split("/")
        # Return new date with correct format
        return f"{year}/{month}/{day}"

if __name__ == "__main__":
    main()