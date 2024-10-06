import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True: 
        level = input("Level: ")
        try:
            level = int(level)
            if level in [1,2,3]:
                return level
            else:
                print("EEE")
        except ValueError:
            print("EEE")

def generate_integer(level):
    for i in range(10):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
            for i in range(3):
                answer = input(f"{x} + {y} = ")
                try:
                    answer = int(answer)
                    if answer == x + y:
                        score += 1
                        break
                    elif answer != x + y and i == 3:
                        print(f"{x} + {y} = {x + y}")
                except ValueError:
                    print("EEE")
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
            for i in range(3):
                answer = input(f"{x} + {y} = ")
                try:
                    answer = int(answer)
                    if answer == x + y:
                        break
                    elif answer != x + y:
                        print("EEE")
                    if answer != x + y and i == 2:
                        print(f"{x} + {y} = {x + y}")
                except ValueError:
                    print("EEE")
                    if answer != x + y and i == 2:
                        print(f"{x} + {y} = {x + y}")
        elif level == 3:
            x = random.randint(100,999)
            y = random.randint(100,999)
            for i in range(3):
                answer = input(f"{x} + {y} = ")
                try:
                    answer = int(answer)
                    if answer == x + y:
                        break
                    elif answer != x + y and i == 3:
                        print(f"{x} + {y} = {x + y}")
                except ValueError:
                    print("EEE")

if __name__ == "__main__":
    main()