import re

# TO-DO: Convert a string like '9:00 AM to 5:00 PM' to '09:00 to 17:00'  
# TO-DO: Convert a string like '9 AM to 5 PM' to '09:00 to 17:00'
# TO-DO: Convert a string like '9:00 AM to 5 PM' to '09:00 to 17:00'
# TO-DO: Convert a string like '9 AM to 5:00 PM' to '09:00 to 17:00'
# TO-DO: Convert a string like '5:00 PM to 9:00 AM' to '09:00 to 17:00'
# TO-DO: Raise ValueError if input is not in correct format like 13:00 PM or 00:00 PM

def main():
    time = input("Hours: ")
    time_converted = convert(time)
    print(time_converted)

def convert(time):
    return time

if __name__ == "__main__":
    main()